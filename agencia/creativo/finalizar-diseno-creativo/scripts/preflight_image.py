#!/usr/bin/env python3
"""Inspect raster image files before graphic-design delivery."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from PIL import Image


def inspect_image(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {"path": str(path.resolve()), "warnings": []}
    try:
        with Image.open(path) as image:
            width, height = image.size
            dpi = image.info.get("dpi")
            icc = image.info.get("icc_profile")
            exif = image.getexif()
            orientation = exif.get(274) if exif else None
            result.update(
                {
                    "format": image.format,
                    "mode": image.mode,
                    "width_px": width,
                    "height_px": height,
                    "aspect_ratio": round(width / height, 4) if height else None,
                    "megapixels": round(width * height / 1_000_000, 2),
                    "dpi": [round(float(v), 2) for v in dpi] if dpi else None,
                    "icc_profile_embedded": bool(icc),
                    "has_alpha": "A" in image.getbands(),
                    "exif_orientation": orientation,
                }
            )
            if min(width, height) < 800:
                result["warnings"].append("El lado corto es menor a 800 px; revisar el tamaño final.")
            if not icc:
                result["warnings"].append("No se detectó un perfil ICC incrustado.")
            if orientation not in (None, 1):
                result["warnings"].append("La orientación depende de EXIF; normalizar antes de entregar.")
            if image.mode in {"P", "1"}:
                result["warnings"].append("Modo de color limitado; revisar degradados y conversión.")
            if dpi and all(float(v) > 0 for v in dpi):
                result["print_size_cm"] = [
                    round(width / float(dpi[0]) * 2.54, 2),
                    round(height / float(dpi[1]) * 2.54, 2),
                ]
            else:
                result["print_size_cm"] = None
    except Exception as exc:  # Surface file-specific failures without stopping a batch.
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


def markdown_report(items: list[dict[str, Any]]) -> str:
    lines = [
        "| Archivo | Formato | Dimensiones | Relación | Color | Perfil | Alertas |",
        "|---|---|---:|---:|---|---|---|",
    ]
    for item in items:
        if "error" in item:
            lines.append(f"| {Path(item['path']).name} | — | — | — | — | — | {item['error']} |")
            continue
        warnings = " ".join(item["warnings"]) or "Sin alertas automáticas"
        lines.append(
            "| {name} | {fmt} | {w}×{h} px | {ratio} | {mode} | {icc} | {warnings} |".format(
                name=Path(item["path"]).name,
                fmt=item["format"] or "—",
                w=item["width_px"],
                h=item["height_px"],
                ratio=item["aspect_ratio"],
                mode=item["mode"],
                icc="Sí" if item["icc_profile_embedded"] else "No",
                warnings=warnings.replace("|", "\\|"),
            )
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Revisar metadatos técnicos de imágenes raster.")
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", help="Emitir JSON en vez de tabla Markdown.")
    args = parser.parse_args()

    results = [inspect_image(path) for path in args.images]
    print(json.dumps(results, ensure_ascii=False, indent=2) if args.json else markdown_report(results))
    return 1 if any("error" in item for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
