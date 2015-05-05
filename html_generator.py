ND_STAGE = ['STAGE 2 PROJECT', 'AUTOMATE YOUR PAGE']
#To automate the page we present documents in list as above.
#I need just the title now, so I'm going to present it as follows

PROJECT = ['STAGE 2 PROJECT: AUTOMATE MY PAGE', ''] 
header = '''
<!DOCTYPE html>
    <!-- The header is not going to change much for now, so it is manual -->
	<!-- This is the beginning of my html -->
<head>
	<title>Okori: NDIP Baby Step Notes</title>
	<link rel="stylesheet" type="text/css" href="css/barry2style.css">
</head>
<body>
	<h1><!-- Always Edit Header Title To fit the Stage! --> ND Stage 2 </h1>
	<div class="lesson"> <!-- opening div for lesson --> '''


footer = '''
<!-- This is the ending html, also not changing much so it is manual -->
	</div> <!-- This is the lesson div ending -->
</body> <!-- This is the body ending -->
</html> <!-- This is the end of the page html --> '''

#code to generate our HTML format
def generate_concept_HTML(concept_title, concept_description):
	html_text_1 = '''
	<div class="concept">
		<div class="concept_title">
			''' + concept_title
	html_text_2 = '''
		</div>
		<div class="concept_description">
			''' + concept_description
	html_text_3 = '''
		</div>
	</div>'''
	full_html_text = html_text_1 + html_text_2 +html_text_3
	return full_html_text


stage2_lesson1 = [[ 'Computer', 'A universal machine that can do whatever we want it to do. But pretty useless without a program'],
	['Computer Program', 'A set of instructions that tell a computer what to do'],
	['Programming Language', 'A language the computer understands, examples are COBOL, Python, C++ etc'],
	['Python', 'Is a higher-level language used to write programs. It is called an <b>Interpreter</b> which means it can run,\
            interpret and execute the programs that we write in Python language '], 
	['Grammer', 'Python is very strict on grammar. No mistake is acceptable, codes must match language grammar exactly.'],
	['Python Expressions', "They are similar to Arithmetic expressions '+', '*' etc. 2 + 2, (2 * (3 + 5) + 7)"],
	['Computation', "A '<b>'Cycle'</b>'  is the time it takes a computer to do one step. A computer does 2.7 billion cycles(2.7GHz) per second"],
        ['Reflection', 'Helps you bridge the knowledge gap between how novices and experts handle materials']]


#baby_1step is like learning to walk, it takes generate_concept_HTML, adds the
#concept title and concept description and generates single HTML for the concept
def baby_1step_HTML(concept):
	concept_title = concept[0]
	concept_description = concept[1]
	return generate_concept_HTML(concept_title, concept_description)

print baby_1step_HTML(PROJECT)

#The following code takes a list of concepts as input and generate HTML for the list of concepts.
def my_baby_steps_HTML(list_of_concepts):
        #This code will generate many concepts for a list of concepts
	HTML =""
	for concept in list_of_concepts:
		concept_HTML = baby_1step_HTML(concept)
		HTML = HTML + concept_HTML
	return HTML
    

#print my_baby_steps_HTML(stage2_lesson1)
#This way I printed each lesson HTML, cut and pasted in my html file

def TEST_many_baby_steps_HTML(list_of_concepts):
	HTML = ""
	for concept in list_of_concepts:
		concept_HTML = baby_1step_HTML(concept)
		HTML = HTML + concept_HTML
	return "HTML PASSED" #For test cases

#The following code takes a lesson as input, adds the header and footer defined
#earlier and returns a page with the lesson, header and footer as output.
def generate_my_page_HTML(concept_list):
	all_html = ''
	for concept in concept_list:
		concept = baby_1step_HTML(concept)
		all_html = all_html + concept
	return header + all_html + footer




#I'm also tried to generate list for my Table of Content with the following
#Lists

def generate_ul_HTML_open(concept): #opening ul
	html_text_1 = '''
	<div class="concept">
		<ul class="concept_title">
			'''
	full_html_text = html_text_1
	return full_html_text


def generate_ul_HTML_close(concept): #for the closing ul
	html_text_1 = '''
		</ul>
	</div> '''
	full_html_text = html_text_1 
	return full_html_text


def generate_list_items(concept): #for the list items
	html_text_1 = '''
		<li><a href="#lesson-0.0"> <!-- Insert lesson id manually -->
			'''  + str(concept)
	html_text_2 = '''
		</a></li> '''
	full_html_text = html_text_1 + html_text_2
	return full_html_text
	    
def generate_all_my_HTML(concept_list):
	all_html = ''
	for concept in concept_list:
		concept = generate_list_items(concept)
		all_html = all_html + concept
	return all_html

#The following code takes the opening and closing list tags above, wrap it around the list items and return an un-ordered list
#There may be a better way but I'm still learning how to improve that.

TOC = ["Lesson 1", "Computer", "Computer Program", "Programming Language", "Programming Language", "Python", "Grammer", "Python Expressions", "Computation", "Reflection"],
["Lesson2", "Variables",  "To assign a value to a variable",
'The difference between the equal signs in <span class="code">2 + 3 = 5</span> and <span class="code">my_variable = 5</span>', "Usefulness of variables",
 'The difference between <span class="code">2 + 2</span> and		<span class="code">"2" + "2"</span>', "The Need for Carefulness" ],
['Lesson 3', 'What is a <span class="bold">function or procedure</span>?',
 "The difference between making and using a function", "How useful are functions to programmers?", "What happens if a function doesn't have a return statement?",
  "Using Functions to Generate HTML"],
["Lesson 4", "The (if) Statement", 'The "While" Loop', "Lists", "List Mutation And Aliasing", "Debugging"],
["Lesson 5", 'List Operations: append(), " + " and len()', "The - For Loop", "List Index", "The - In Operation", "How to Solve Problems"]



    
def generate_all_list_html(concept_list):
	return generate_ul_HTML_open(concept_list) +'' +generate_all_my_HTML(concept_list) + generate_ul_HTML_close(concept_list)

#print generate_all_list_html(TOC)
#Note: I didn't include the TOC on my final work as it still requires lot of manual works


#This following codes will
#1. The first one tests that the code and text provided works
#2. The second code will generate HTML for stage2, lesson 1 with opening and closing HTML tags that I can copy and paste
    
print TEST_many_baby_steps_HTML(stage2_lesson1)

print generate_my_page_HTML(stage2_lesson1)
#Most of my codes are based on class example codes by ANDY and a few alterations.
