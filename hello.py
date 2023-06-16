from urllib3.util.ssl_ import SSLContext
from urllib3.util.ssl_ import OP_NO_SSLv2

def create_urllib3_context():
    context = SSLContext()

    options = 0
    # SSLv2 is easily broken and is considered harmful and dangerous
    options |= OP_NO_SSLv2
    context.options |= options

def main():
    print("About to create a urllib3 context")
    context = create_urllib3_context()
    print(f"How about that context, eh? {context}")

if __name__ == "__main__":
    main()
