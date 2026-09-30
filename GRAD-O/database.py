import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_db_connection():
    """Establish connection to PostgreSQL."""
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return connection
    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None

def add_student(student_number, first_name, middle_name, last_name, phinmaed_email):
    """Insert a new student into the 'student' table."""
    conn = get_db_connection()
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO student (
                student_number, 
                first_name, 
                middle_name, 
                last_name, 
                phinmaed_email
            )
            VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(query, (
            student_number, 
            first_name, 
            middle_name, 
            last_name, 
            phinmaed_email
        ))
        
        conn.commit()
        cursor.close()
        print("Student record inserted successfully!")
        return True
    except Exception as e:
        print(f"Error inserting student: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def create_grades_table():
    """Ensure the student_grades table exists in PostgreSQL."""
    conn = get_db_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_grades (
                grade_id BIGSERIAL PRIMARY KEY,
                student_id BIGINT NOT NULL,
                subject_code VARCHAR(20) NOT NULL,
                written_score NUMERIC(5, 2) DEFAULT 0.00,
                quiz_score NUMERIC(5, 2) DEFAULT 0.00,
                exam_score NUMERIC(5, 2) DEFAULT 0.00,
                final_grade NUMERIC(5, 2) NOT NULL,
                grade_point NUMERIC(3, 2) NOT NULL,
                remarks VARCHAR(20) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                CONSTRAINT fk_student 
                    FOREIGN KEY (student_id) 
                    REFERENCES student(id) 
                    ON DELETE CASCADE,
                CONSTRAINT unique_student_subject UNIQUE (student_id, subject_code)
            );
        """)
        conn.commit()
        cursor.close()
        print("Grades table initialized successfully!")
    except Exception as e:
        print(f"Error creating grades table: {e}")
    finally:
        conn.close()
