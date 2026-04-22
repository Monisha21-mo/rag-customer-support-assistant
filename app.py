from src.ingest import load_and_split
from src.retriever import create_retriever
from src.graph import run_graph

def main():
    pdf_path = "file.pdf"   # your uploaded PDF

    print("Loading document...")
    chunks = load_and_split(pdf_path)

    print("Creating retriever...")
    retriever = create_retriever(chunks)

    print("\nSystem ready! Type 'exit' to quit.\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            print("Exiting...")
            break

        result = run_graph(query, retriever)
        print(result)
        print()

if __name__ == "__main__":
    main()
