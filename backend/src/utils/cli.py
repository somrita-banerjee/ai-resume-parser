import click
import json
import os
from .extractor import extract_text
from parser import parse_resume_text

@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.option("--outdir", "-o", default="data/parsed_outputs", help="Output directory")
def main(input_path, outdir):
    text = extract_text(input_path)
    parsed = parse_resume_text(text)
    os.makedirs(outdir, exist_ok=True)

    filename = os.path.basename(input_path)
    outpath = os.path.join(outdir, f"parsed_{filename}.json")

    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(parsed.__dict__, f, default=lambda o: o.__dict__, indent=2)

    click.echo(f"✅ Parsed resume saved to {outpath}")

if __name__ == "__main__":
    main()
