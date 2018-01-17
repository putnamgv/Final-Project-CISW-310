#!/usr/bin/perl
use DBI;
use CGI ':standard';
require "subroutine.lib";


# Connect to the database through DBI
# &dbcon();

# ***ATTENTION***  Below line is commented out for security purposes and will need to be updated once connecting to MySQL

#   $dbh = DBI->connect("DBI:mysql:[username]", "[username]", '[password]');


&mime();

# Begin FIRST HERE statement

print <<MYFORM;

<html>
<head>
<meta charset='UTF-8'>
<script>

function validateLogin(form) 
{
var reName = /^[a-zA-Z]+\$\/

// first name - Make certain there is only 1 name in the box for First Name and Last Name and it is made up of letters only.

if(!reName.test(form.fname.value))
	{
	alert("Please Type a First Name");
	return false;
	}
if(!reName.test(form.lname.value))
	{
	alert("Please Type a Last Name");
	return false;
	}
if(form.password.value=='')
	{
	alert("Please Type a Password");
	return false;
	}
return true;
}	

function validateQuiz(form) 
{
// Make certain they select an answer to each question

//Question 1

	var question_1 = -1;
	for(i = 0; i < form.question1.length; i++)
	{
		if(form.question1[i].checked)
		{
		question_1 = i;
		}
	}
	if(question_1 == -1)
	{
	alert("Please select an answer to question 1");
	return false;
	}
	
//Question 2

	var question_2 = -1;
	for(i = 0; i < form.question2.length; i++)
	{
		if(form.question2[i].checked)
		{
		question_2 = i;
		}
	}
	if(question_2 == -1)
	{
	alert("Please select an answer to question 2");
	return false;
	}
	
	
//Question 3

	var question_3 = -1;
	for(i = 0; i < form.question3.length; i++)
	{
		if(form.question3[i].checked)
		{
		question_3 = i;
		}
	}
	if(question_3 == -1)
	{
	alert("Please select an answer to question 3");
	return false;
	}
	
//Question 4

	var question_4 = -1;
	for(i = 0; i < form.question4.length; i++)
	{
		if(form.question4[i].checked)
		{
		question_4 = i;
		}
	}
	if(question_4 == -1)
	{
	alert("Please select an answer to question 4");
	return false;
	}

//Question 5

	var question_5 = -1;
	for(i = 0; i < form.question5.length; i++)
	{
		if(form.question5[i].checked)
		{
		question_5 = i;
		}
	}
	if(question_5 == -1)
	{
	alert("Please select an answer to question 5");
	return false;
	}
	
	
//Question 6

	var question_6 = -1;
	for(i = 0; i < form.question6.length; i++)
	{
		if(form.question6[i].checked)
		{
		question_6 = i;
		}
	}
	if(question_6 == -1)
	{
	alert("Please select an answer to question 6");
	return false;
	}

	
//Question 7

	var question_7 = -1;
	for(i = 0; i < form.question7.length; i++)
	{
		if(form.question7[i].checked)
		{
		question_7 = i;
		}
	}
	if(question_7 == -1)
	{
	alert("Please select an answer to question 7");
	return false;
	}

return true;
}

</script>


<title>Cisw 310 - Chris Putnam's Project</title>
</head>
<body>

<a href="project.cgi?takequiz=yes">Take Quiz</a>
<a href="project.cgi?seescore=yes">See Score</a>

MYFORM

# End FIRST HERE statement

$takequiz=param('takequiz');
if ($takequiz)
{
print '<br>
<form method="post" action="project.cgi" onsubmit="return validateLogin(this)">
<fieldset>
<legend>Create Account</legend>
<input type="text" name="fname">First Name<br><br>
<input type="text" name="lname">Last Name<br><br>
<input type="text" name="password">Password<br><br>
<input type="submit" name="takequiz2" value="Start Quiz">
</fieldset>
</form>';
}

$takequiz2=param('takequiz2');

if ($takequiz2)
{

$fname = param('fname');
$lname = param('lname');
$password = param('password');

$query = $dbh->prepare("select * from myquizzes where fname='$fname' and lname='$lname' and password='$password'");
$query->execute;

$num = $query->rows;

if ($num == 0)
{

print <<SHOWQUIZ;

<form method="post" action="project.cgi" onsubmit="return validateQuiz(this)">
<fieldset>
<legend>The Quiz</legend>
<!-- param in hidden variable -->
<input type="hidden" name="fname" value="$fname">
<input type="hidden" name="lname" value="$lname">
<input type="hidden" name="password" value="$password">


<!-- QUESTION 1 -->
<h3>What is the capital of Noth Dakota:</h3>
<input type="radio" name="question1" value="A">Fargo 
<input type="radio" name="question1" value="B">Bismark
<input type="radio" name="question1" value="C">Grand Forks
<input type="radio" name="question1" value="D">Minot 

<!-- QUESTION 2 -->
<h3>What is the capital of South Carolina:</h3>
<input type="radio" name="question2" value="A">Charleston 
<input type="radio" name="question2" value="B">Mount Pleasant  
<input type="radio" name="question2" value="C">Florence 
<input type="radio" name="question2" value="D">Columbia

<!-- QUESTION 3 -->
<h3>What is the capital of South Dakota:</h3>
<input type="radio" name="question3" value="A">Pierre 
<input type="radio" name="question3" value="B">Sioux Falls
<input type="radio" name="question3" value="C">Rapid City 
<input type="radio" name="question3" value="D">Deadwood  

<!-- QUESTION 4 -->
<h3>What is the capital of Vermont:</h3>
<input type="radio" name="question4" value="A">Montpelier
<input type="radio" name="question4" value="B">Brattleboro
<input type="radio" name="question4" value="C">Burlington 
<input type="radio" name="question4" value="D">Rutland  

<!-- QUESTION 5 -->
<h3>What is the capital of Virginia:</h3>
<input type="radio" name="question5" value="A">Williamsburg 
<input type="radio" name="question5" value="B">Norfolk  
<input type="radio" name="question5" value="C">Charlottesville 
<input type="radio" name="question5" value="D">Richmond  

<!-- QUESTION 6 -->
<h3>What is the capital of West Virginia:</h3>
<input type="radio" name="question6" value="A">Weirton 
<input type="radio" name="question6" value="B">Huntington  
<input type="radio" name="question6" value="C">Charleston
<input type="radio" name="question6" value="D">Morgantown  

<!-- QUESTION 7 -->
<h3>What is the capital of Wyoming:</h3>
<input type="radio" name="question7" value="A">Casper 
<input type="radio" name="question7" value="B">Cheyenne 
<input type="radio" name="question7" value="C">Rock Springs
<input type="radio" name="question7" value="D">Laramie  



<br><br>

<!-- Quiz Submit -->
<input type="submit" name="takequiz3" value="Submit">

</form>

<br>


SHOWQUIZ

	}
	else 
	{
	print "<h2>$fname $lname has already taken the state capital quiz</h2>";
	}
}

$takequiz3=param('takequiz3');

if ($takequiz3)
{


$fname = param('fname');
$lname = param('lname');
$password = param('password');
$question1 = param('question1');
$question2 = param('question2');
$question3 = param('question3');
$question4 = param('question4');
$question5 = param('question5');
$question6 = param('question6');
$question7 = param('question7');

$score = 0;

	if($question1 eq "B")
	{
		$score++;
	}	
	if($question2 eq "D")
	{
		$score++;
	}
	if($question3 eq "A")
	{
		$score++;
	}	
	if($question4 eq "A")
	{
		$score++;
	}	
	if($question5 eq "D")
	{
		$score++;
	}
	if($question6 eq "C")
	{
		$score++;
	}
	if($question7 eq "B")
	{
		$score++;
	}
	
$query = $dbh->prepare("insert into myquizzes values('', '$fname', '$lname', '$password', CURRENT_DATE, CURRENT_TIME, '$score')");

$query->execute;

$query2 = $dbh->prepare('select * from myquizzes order by dateoftest, timeoftest');
$query2->execute;

print "<h2>$fname $lname your score was $score<h2>";


print "<table border='1'>";

	while(@row = $query2->fetchrow_array)
	{
	($id, $fname, $lname, $password, $date, $time, $score) = (@row);
	print "<tr><td>$fname $lname</td><td>$date $time</td><td>$score</td></tr>";
	}
print "</table>";
}



$seescore = param('seescore');

if($seescore)
	{
	print '<br><form method="post" action="project.cgi" onsubmit="return validateLogin(this)">
	<fieldset>
	<legend>Login</legend>
	<input type="text" name="fname">First Name<br><br>
	<input type="text" name="lname">Last Name<br><br>
	<input type="text" name="password">Password<br><br>
	<input type="submit" name="seescore2" value="See Score">
	</fieldset>
	</form>';
	}

$seescore2 = param('seescore2');
if($seescore2)

{
$fname = param('fname');
$lname = param('lname');
$password = param('password');

$query = $dbh->prepare("select * from myquizzes where fname='$fname' and lname='$lname' and password='$password'");
$query->execute;

$num = $query->rows;
	if($num == 0)
	{
	print "<h2>You have not yet taken the stsate capital quiz</h2>";
	}
	else
	{
	$query2 = $dbh->prepare('select * from myquizzes order by dateoftest, timeoftest');
	$query2->execute;

	print "<h2>The scores are:<h2>";


	print "<table border='1'>";

		while(@row = $query2->fetchrow_array)
		{
		($id, $fname, $lname, $password, $date, $time, $score) = (@row);
		print "<tr><td>$fname $lname</td><td>$date $time</td><td>$score</td></tr>";
		}
	print "</table>";
	}
	
}




&footer();
