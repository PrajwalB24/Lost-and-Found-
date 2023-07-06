import pickle
from pathlib import Path

import streamlit_authenticator as sa

names = ["Pranav","Rajat","Prajwal"]
username = ["Pranav123","Rajat123","Prajwal123"]
password = ["Pranav","Rajat","Prajwal"]

hashed_passwords = sa.Hasher(password).generate()

file_path = Path(__file__).parent / "hashed_passwords.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)