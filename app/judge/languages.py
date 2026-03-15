LANGUAGES = {
    "python": {
        "filename": "main.py",
        "compile": None,
        "run": ["python3", "main.py"]
    },

    "cpp": {
        "filename": "main.cpp",
        "compile": ["g++", "main.cpp", "-O2", "-o", "main"],
        "run": ["./main"]
    },

    "java": {
        "filename": "Main.java",
        "compile": ["javac", "Main.java"],
        "run": ["java", "Main"]
    },

    "go": {
        "filename": "main.go",
        "compile": ["go", "build", "-o", "main", "main.go"],
        "run": ["./main"]
    }
}