from pathlib import Path
import pandas as pd
import re

RAW_DIR = Path("data/raw")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# strips spaces/slashes/brackets
def snake_cols(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns={
        c: c.strip().replace("(", "").replace(")", "").replace("/", "_").replace(" ", "_").lower()
        for c in df.columns
    })

# trimming whitespace & normalise empty strings to None for every object col
def strip_strings(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip().replace({"": None, "nan": None})
    return df

# removing duplicate rows and rows whose PK is null
def drop_dupes_and_null_pk(df: pd.DataFrame, pk: str) -> pd.DataFrame:
    return df.drop_duplicates().dropna(subset=[pk])

def to_nullable_int(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce").round().astype("Int64")

def map_ids(df: pd.DataFrame, id_col: str, new_col: str) -> pd.DataFrame:
    id_map = df[[id_col]].drop_duplicates().reset_index(drop=True)
    id_map[new_col] = id_map.index + 1
    return df.merge(id_map, on=id_col, how="left"), id_map

# ─────────────────────────────────────────────────────────────
# CLEANING ALL CSV BEGINS FROM HERE
# ─────────────────────────────────────────────────────────────
print("Cleaning authors.csv …")
authors = pd.read_csv(RAW_DIR / "author.csv")
authors = snake_cols(authors)
authors = strip_strings(authors)
authors = drop_dupes_and_null_pk(authors, "author_id")
authors, author_id_map = map_ids(authors, "author_id", "author_int_id")

print("Cleaning topic.csv …")
topics = pd.read_csv(RAW_DIR / "topic.csv")
topics = snake_cols(topics)
topics = strip_strings(topics)
topics = drop_dupes_and_null_pk(topics, "topic_id")
topics, topic_id_map = map_ids(topics, "topic_id", "topic_int_id")

print("Cleaning journal.csv …")
journals = pd.read_csv(RAW_DIR / "journal.csv")
journals = snake_cols(journals)
journals = strip_strings(journals)
journals = journals.drop_duplicates(subset=["journal_name"])

print("Cleaning paper.csv …")
papers = pd.read_csv(RAW_DIR / "paper.csv", low_memory=False)
papers = snake_cols(papers)
papers = strip_strings(papers)
papers = drop_dupes_and_null_pk(papers, "paper_id")
papers, paper_id_map = map_ids(papers, "paper_id", "paper_int_id")
papers["paper_year"] = to_nullable_int(papers["paper_year"])
papers["paper_citation_count"] = to_nullable_int(papers["paper_citation_count"])
papers["journal_volume"] = to_nullable_int(papers["journal_volume"])

print("Cleaning author_paper.csv …")
author_paper = pd.read_csv(RAW_DIR / "author_paper.csv")
author_paper = snake_cols(author_paper)
author_paper = strip_strings(author_paper)
author_paper = author_paper.drop_duplicates()
author_paper = author_paper.merge(author_id_map, on="author_id", how="inner")
author_paper = author_paper.merge(paper_id_map, on="paper_id", how="inner")

print("Cleaning paper_topic.csv …")
paper_topic = pd.read_csv(RAW_DIR / "paper_topic.csv")
paper_topic = snake_cols(paper_topic)
paper_topic = strip_strings(paper_topic)
paper_topic = paper_topic.drop_duplicates()
paper_topic = paper_topic.merge(paper_id_map, on="paper_id", how="inner")
paper_topic = paper_topic.merge(topic_id_map, on="topic_id", how="inner")

print("Cleaning paper_journal.csv …")
paper_journal = pd.read_csv(RAW_DIR / "paper_journal.csv")
paper_journal = snake_cols(paper_journal)
paper_journal = strip_strings(paper_journal)
paper_journal = paper_journal.drop_duplicates()
paper_journal = paper_journal.merge(paper_id_map, on="paper_id", how="inner")
paper_journal = paper_journal[paper_journal["journal_name"].isin(journals["journal_name"])]

print("Cleaning paper_reference.csv …")
paper_reference = pd.read_csv(RAW_DIR / "paper_reference.csv")
paper_reference = snake_cols(paper_reference)
paper_reference = strip_strings(paper_reference)
paper_reference = paper_reference.drop_duplicates()
paper_reference = paper_reference.merge(
    paper_id_map.rename(columns={"paper_id": "paper_id", "paper_int_id": "paper_int_id"}),
    on="paper_id", how="inner"
).merge(
    paper_id_map.rename(columns={"paper_id": "referenced_paper_id", "paper_int_id": "referenced_paper_int_id"}),
    on="referenced_paper_id", how="inner"
)

authors.to_csv(OUT_DIR / "author_cleaned.csv", index=False)
topics.to_csv(OUT_DIR / "topic_cleaned.csv", index=False)
journals.to_csv(OUT_DIR / "journal_cleaned.csv", index=False)
papers.to_csv(OUT_DIR / "paper_cleaned.csv", index=False)
author_paper.to_csv(OUT_DIR / "author_paper_cleaned.csv", index=False)
paper_topic.to_csv(OUT_DIR / "paper_topic_cleaned.csv", index=False)
paper_journal.to_csv(OUT_DIR / "paper_journal_cleaned.csv", index=False)
paper_reference.to_csv(OUT_DIR / "paper_reference_cleaned.csv", index=False)

print("\n  all csvs cleaned!")
