from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Goswami",
    author_email="goswamiayush201@gmail.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","pyPDF2"],
    packages=find_packages()
)