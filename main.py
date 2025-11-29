from dotenv import load_dotenv  # Memanggil API_KEY pada file .env (Berbagai macam file mungkin bisa dipanggil)
#import os                       # Berinteraksi dengan sistem operasi seperti melalui cmd/terminal

load_dotenv()


def main():
    print("Hello from langchain-course!")
#    print(os.environ.get("GOOGLE_API_KEY"))    # untuk Cek apakah kita bisa memanggil API KEY dari .env


if __name__ == "__main__":
    main()
