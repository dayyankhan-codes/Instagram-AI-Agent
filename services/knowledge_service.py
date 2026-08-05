from pathlib import Path


def load_knowledge():

    knowledge_folder = Path("knowledge")

    knowledge = ""

    for file in knowledge_folder.glob("*.md"):

        knowledge += file.read_text(
            encoding="utf-8"
        )

        knowledge += "\n\n"

    return knowledge