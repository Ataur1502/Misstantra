from models import Question  # Replace 'quizapp' with your app name

# List of new question dictionaries
questions = [
    {"text": "What will be the output or behavior of this code?", "option_a": "Causes error", "option_b": "Input shows 'Hello World' but cannot be edited", "option_c": "Input editable", "option_d": "Hidden field", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "'Hello World' is bold for 'World' only", "option_b": "All is bold", "option_c": "Nothing displayed", "option_d": "Both lines are bold", "correct_answer": "A", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "All in blue", "option_b": "\"Welcome\" in blue and \"to the site\" in red", "option_c": "All in red", "option_d": "No color applied", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "No output", "option_b": "Shows numbered list", "option_c": "Display a bulleted list", "option_d": "Displays inline", "correct_answer": "C", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Shows 'home.html' as", "option_b": "opens in same tab", "option_c": "Opens home.html in a new tab", "option_d": "Does not work", "correct_answer": "C", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Invisible", "option_b": "is red", "option_c": "black", "option_d": "is blue", "correct_answer": "D", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Adds only padding", "option_b": "Adds only margin", "option_c": "Adds 10px margin and 5px padding", "option_d": "Adds border", "correct_answer": "C", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Adds margin", "option_b": "Adds 1px solid black border", "option_c": "Changes color", "option_d": "Adds padding", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Font size remains default", "option_b": "Font size is 20px", "option_c": "Becomes bold", "option_d": "No change is display", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Adds border", "option_b": "Adds only padding", "option_c": "Adds 10px margin and 5px padding", "option_d": "Adds only margin", "correct_answer": "C", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Width 200px", "option_b": "Width auto", "option_c": "No display", "option_d": "Width is 100px", "correct_answer": "D", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Color changes to blue", "option_b": "Background is lightblue", "option_c": "Adds border", "option_d": "Centers the text", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Centers child elements both ways", "option_b": "Aligns left", "option_c": "Centers only horizontally", "option_d": "Center only vertically", "correct_answer": "A", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Width set to 100px", "option_b": "Height is 100px", "option_c": "no visual change", "option_d": "Adds padding", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "undefined", "option_b": "error", "option_c": "FALSE", "option_d": "TRUE", "correct_answer": "D", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "TRUE", "option_b": "FALSE", "option_c": "Undefined", "option_d": "Error", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Prints 0 only", "option_b": "Prints 0 then 1", "option_c": "Error", "option_d": "Print 2", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Outputs 51", "option_b": "nan", "option_c": "Outputs 6", "option_d": "Error", "correct_answer": "C", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Outputs undefined", "option_b": "Outputs 7", "option_c": "Error", "option_d": "Outputs 5", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "3", "option_b": "1", "option_c": "0", "option_d": "10", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "hello", "option_b": "HELLO", "option_c": "Error", "option_d": "Undefined", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "FALSE", "option_b": "Error", "option_c": "Undefined", "option_d": "TRUE", "correct_answer": "A", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "object", "option_b": "array", "option_c": "Undefined", "option_d": "string'", "correct_answer": "A", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "array", "option_b": "list", "option_c": "object", "option_d": "Undefined", "correct_answer": "C", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "[3]", "option_b": "[1, 2, 3]", "option_c": "[]", "option_d": "[1,2]", "correct_answer": "D", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "FALSE", "option_b": "TRUE", "option_c": "Error", "option_d": "Null", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "3", "option_b": "1", "option_c": "Undefined", "option_d": "Error", "correct_answer": "A", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Nothing shown", "option_b": "False shown", "option_c": "Error", "option_d": "Displays 'Visible'", "correct_answer": "D", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Shows <h1> tag", "option_b": "Renders a heading 'Hello'", "option_c": "Nothing", "option_d": "Error", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Decrements state", "option_b": "Throws error", "option_c": "no change", "option_d": "Increments state value by 1", "correct_answer": "D", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Never logs", "option_b": "Logs 'hi' once after mount", "option_c": "Logs repeatedly", "option_d": "Logs before render", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Error", "option_b": "Immediately prints", "option_c": "Prints 'done' after 1s delay", "option_d": "Prints nothing", "correct_answer": "C", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Current working directory", "option_b": "Node.js version string", "option_c": "Error", "option_d": "Platform name", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "File name", "option_b": "error", "option_c": "Root dir", "option_d": "Prints current directory path", "correct_answer": "D", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "dir1/file.js", "option_b": "dir1file.js", "option_c": "Error", "option_d": "dir1 + file.js", "correct_answer": "A", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Prints 'tick' once after 1s", "option_b": "error", "option_c": "Prints 'tick' repeatedly every 1s", "option_d": "Prints nothing", "correct_answer": "C", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Script file name", "option_b": "Current working directory path", "option_c": "Root directory", "option_d": "Error", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Starts an HTTP server on port 3000", "option_b": "Prints server details", "option_c": "Error without callback", "option_d": "No server started", "correct_answer": "A", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Nothing", "option_b": "error", "option_c": "Prints OS platform like 'win32'", "option_d": "Undefined", "correct_answer": "C", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "prints 'test' event", "option_b": "Error: no listener attached", "option_c": "Starts event loop", "option_d": "Defines event", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Deleted file", "option_b": "Checks if file exists", "option_c": "Throws error", "option_d": "Creates file", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Creates DataFrame with 2rows, 2columns", "option_b": "Error", "option_c": "Creates list", "option_d": "Empty frame", "correct_answer": "A", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Error", "option_b": "6", "option_c": "[1, 2, 3]", "option_d": "Creates Dataframe", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Trains immediately", "option_b": "Predicts output", "option_c": "Error", "option_d": "Creates regression model instance", "correct_answer": "D", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Error", "option_b": "1", "option_c": "6", "option_d": "2", "correct_answer": "D", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Deletes input", "option_b": "Splits data into train and test sets", "option_c": "Normalizes data", "option_d": "Combines arrays", "correct_answer": "B", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Error", "option_b": "None", "option_c": "print tensor([2, 4.])", "option_d": "[1,2]", "correct_answer": "C", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Generates image", "option_b": "Silent", "option_c": "Error", "option_d": "Display msgs", "correct_answer": "D", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Loads a generation model", "option_b": "Creates dataset", "option_c": "Error", "option_d": "Loads vision model", "correct_answer": "A", "marks": 1},
    {"text": "What will be the output or behavior of this code?", "option_a": "Example of simple generation", "option_b": "Image generation", "option_c": "Example of translation", "option_d": "Speech recognition", "correct_answer": "A", "marks": 1},
]

# Insert into DB
count = 0
for q in questions:
    try:
        Question.objects.create(
            text=q["text"],
            option_a=q["option_a"],
            option_b=q["option_b"],
            option_c=q["option_c"],
            option_d=q["option_d"],
            correct_answer=q["correct_answer"],
            marks=q["marks"]
        )
        count += 1
    except Exception as e:
        print(f"❌ Failed to insert question: {q['text'][:60]}... Error: {e}")

print(f"✅ Successfully inserted {count} questions into the database.")
