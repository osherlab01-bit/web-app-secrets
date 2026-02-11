<?php
$username = $_POST['username'];
$password = $_POST['password'];

// VULNERABLE: SQL Injection
$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysql_query($query);
?>
