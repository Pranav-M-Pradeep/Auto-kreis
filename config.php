<?php
$host = "localhost"; // Change if using a different host
$user = "root"; // Change if your MySQL user is different
$password = "SQL@rakhi"; // Add your MySQL password if you have set one
$database = "Autokries"; // Your database name

$conn = new mysqli($host, $user, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
