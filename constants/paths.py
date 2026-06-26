from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"

ARCHIVES = BASE_DIR / "archives"

EXPORTS = ARCHIVES / "exports"

IMPORTS = ARCHIVES / "imports"


EXPORT_CONTAGEM_ESTOQUE = EXPORTS / "contagem_estoque"

EXPORT_CONTAGEM_ESTOQUE_DOCES = EXPORTS / "contagem_estoque_doces"

EXPORT_CONTAGEM_DATAS = EXPORTS / "contagem_datas"

EXPORT_CONTAGEM_GELADEIRAS = EXPORTS / "contagem_geladeiras"