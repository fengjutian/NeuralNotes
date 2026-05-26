#!/usr/bin/env python
"""Simple server runner."""
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_dirs=["d:/GitHub/NeuralNotes/backend"],
    )
