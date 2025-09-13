<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hostel Management System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background: linear-gradient(to right, #4facfe, #00f2fe);
            color: white;
            text-align: center;
            padding: 20px;
        }
        .nav {
            display: flex;
            justify-content: space-around;
            background: #333;
            color: white;
            padding: 10px;
        }
        .nav a {
            color: white;
            text-decoration: none;
            font-size: 18px;
        }
        .nav a:hover {
            text-decoration: underline;
        }
        .main {
            text-align: center;
            padding: 20px;
            background: #f9f9f9;
            min-height: 80vh;
        }
        .button {
            background-color: #4caf50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-transform: uppercase;
            border-radius: 5px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #45a049;
        }
        .section {
            display: flex;
            justify-content: space-evenly;
            flex-wrap: wrap;
            margin-top: 20px;
        }
        .card {
            background: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            padding: 20px;
            width: 300px;
            margin: 10px;
            text-align: left;
            border-radius: 8px;
        }
        .footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 10px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Welcome to Our Hostel Management System</h1>
        <p>Book your stay, enjoy our facilities, and feel at home!</p>
    </div>

    <div class="nav">
        <a href="#bookings">Bookings</a>
        <a href="#gym">Gym</a>
        <a href="#food">Food Facility</a>
        <a href="#rooms">Rooms</a>
        <a href="#contact">Contact Us</a>
    </div>

    <div class="main">
        <h2 id="bookings">Bookings</h2>
        <p>Book your room easily and securely.</p>
        <button class="button">Book Now</button>

        <div class="section">
            <div class="card">
                <h3>Gym</h3>
                <p>Stay fit and healthy with our fully equipped gym.</p>
                <button class="button">Explore Gym</button>
            </div>
            <div class="card">
                <h3>Food Facility</h3>
                <p>Delicious meals are provided to ensure your comfort.</p>
                <button class="button">View Menu</button>
            </div>
            <div class="card">
                <h3>Rooms</h3>
                <p>Choose from AC and Non-AC rooms as per your preference.</p>
                <button class="button">Check Availability</button>
            </div>
        </div>
    </div>

    <div class="footer">
        <p>&copy; 2024 Hostel Management System. All rights reserved.</p>
    </div>
</body>
</html>
