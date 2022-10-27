import sqlite3
import pandas as pd
import streamlit as st

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base

engine = create_engine("sqlite:///bce.db")

Base.metadata.create_all(engine)

session = Session()
