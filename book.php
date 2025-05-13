<?php
$servername = "localhost";
$username = "root";  // Default XAMPP username
$password = "SQL@rakhi";      // Default XAMPP password (empty)
$dbname = "Autokries";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$user_id = $_POST['user_id'];
$service_date = $_POST['date'];   // Change 'date' to 'service_date'
$service_time = $_POST['time'];
$service_needed = $_POST['service_needed'];
$service_notes = $_POST['notes'];

// Prepare and bind SQL statement
$sql = "INSERT INTO bookings (user_id, service_date, service_time, service_needed, service_notes) 
        VALUES (?, ?, ?, ?, ?)";

$stmt = $conn->prepare($sql);
$stmt->bind_param("sssss", $user_id, $service_date, $service_time, $service_needed, $service_notes);

// Execute the query
if ($stmt->execute()) {
    header("Location: payment.html");
    exit();
} else {
    echo "Error: " . $stmt->error;
}

// Close connection
$stmt->close();
$conn->close();
?>
