import os
import glob
import sqlite3
import pyfiglet
import subprocess

con =  sqlite3.connect("authoiOnlineJudge.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS problems (problem, result, test)")

def add_problem(problem_text,result, test):
    cur.execute(
        "INSERT INTO problems (problem, result, test) VALUES (:problem, :result, :test)",
        {"problem": problem_text, "result": result, "test": test}
    )
    con.commit()

def pick_problem():
    cur.execute("SELECT * FROM problems ORDER BY RANDOM() LIMIT 1;")
    row = cur.fetchone()
    return {"problem": row[0], "result": row[1], "test": row[2]}

def show_problem():
    programming_problem = pick_problem()
    print(programming_problem["problem"])
    return programming_problem

def submit_answer(base_dir, file_name, problem):
    file_path = os.path.join(base_dir, file_name)
    code_file = glob.glob(file_path)

    print(code_file)
    print("We got the file!🎇")
    print("File Verified🎉")

    extension = "node" if file_name.endswith(".js") else "python" if file_name.endswith(".py") else None
    if extension == None :
        raise ValueError("file type not supported. Only js and py files are supported")
    
    try:
        result = subprocess.run([extension,file_path], capture_output=True, input=problem["test"].encode('utf-8'))
    except Exception as e:
        print(f"{type(e)}! -> {e}")
        return

    if result.stdout.decode("utf-8").strip() == problem["result"]:
        print("CONGRATULATION 🎉 YOUR ANSWER HAS ACCEPTED ✨✅")
        return "CONGRATULATION 🎉 YOUR ANSWER HAS ACCEPTED ✨✅"
    else:
        print("Wrong Answer")
        return "Wrong Answer"

if __name__ == "__main__":
    print(pyfiglet.figlet_format("WELCOME", font = "5lineoblique" ))
    print(pyfiglet.figlet_format("IN", font = "5lineoblique" ))
    print(pyfiglet.figlet_format("AUTHOI   ONLINE   JUDGE", font = "5lineoblique" ))
    print("NOTE: Only JS and Python files are allowed")

    add_problem("Make a function that Takes a string as input and print it's reversed version. Call the function inside the code . print the result.", "ijibijih", "hijibiji")

    problem = show_problem()

    submit_answer("E:\\Project (old)\\PythonSuperAdvancedPractice\\hudahui", "def.py", problem)


con.commit()
cur.close()
con.close()