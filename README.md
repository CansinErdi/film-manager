# Film Collection Manager

A Python-based Film Collection Manager using MySQL to store and manage film data. The system allows adding, updating, deleting, and searching for films, with a focus on George Lucas' film collection.

## Table of Contents
- [Project Overview](#project-overview)
- [Setup](#setup)
  - [MySQL Installation](#mysql-installation)
  - [Creating the Database and Table](#creating-the-database-and-table)
  - [Inserting Films](#inserting-films)
- [Running the Script](#running-the-script)
- [Usage](#usage)

## Project Overview

This project uses Python to interact with a MySQL database to manage a film collection. It includes a pre-configured set of George Lucas films.

## Setup

### MySQL Installation

Install MySQL and ensure it is running. Add MySQL to the system PATH for easy access from the terminal.

### Creating the Database and Table

Run the following commands in MySQL to set up the database and table:

```sql
CREATE DATABASE film_collection;
USE film_collection;

CREATE TABLE films (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    director VARCHAR(255),
    genre VARCHAR(100),
    release_year INT,
    rating FLOAT
);

INSERT INTO films (title, director, genre, release_year, rating)
VALUES 
('Star Wars: A New Hope', 'George Lucas', 'Science Fiction', 1977, 8.6),
('Star Wars: The Empire Strikes Back', 'Irvin Kershner (Produced by George Lucas)', 'Science Fiction', 1980, 8.7),
-- Additional films go here...

## Inserting Films

### Insert George Lucas' films into the database:

INSERT INTO films (title, director, genre, release_year, rating)
VALUES 
('Star Wars: A New Hope', 'George Lucas', 'Science Fiction', 1977, 8.6),
('Star Wars: The Empire Strikes Back', 'Irvin Kershner (Produced by George Lucas)', 'Science Fiction', 1980, 8.7),
-- Additional films go here...

## Running the Script

### Ensure you have Python and the mysql-connector-python package installed:

pip install mysql-connector-python
python film_manager.py


## Usage

### The script allows adding, deleting, updating, and searching films in the film_collection database.


This version keeps things brief and to the point while still covering the key steps. You can customize or add more details based on your project needs!

