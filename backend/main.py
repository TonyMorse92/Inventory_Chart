from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Required for cross-origin requests


app = FastAPI()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
	return {"Hello": "World"}


def fib_n(n: int):
	if n < 2:
		return 1
	else:
		return fib_n(n-1) + fib_n(n-2)

@app.get("/fib/{n}")
def read_fib(n: int):
	return {"fib_n": fib_n(n)}


@app.get("/data/")
def read_root():
	return [{"date": "2024-11-11", "value": 113},
{"date": "2024-11-12", "value": 362},
{"date": "2024-11-13", "value": 442},
{"date": "2024-11-14", "value": 211},
{"date": "2024-11-15", "value": 107},
{"date": "2024-11-16", "value": 277},
{"date": "2024-11-17", "value": 162},
{"date": "2024-11-18", "value": 400},
{"date": "2024-11-19", "value": 106},
{"date": "2024-11-20", "value": 262},
{"date": "2024-11-21", "value": 368},
{"date": "2024-11-22", "value": 543},
{"date": "2024-11-23", "value": 491},
{"date": "2024-11-24", "value": 500},
{"date": "2024-11-25", "value": 485},
{"date": "2024-11-26", "value": 117}
]
