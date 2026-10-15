login = {
    "hint": "Authenticate with Google Calendar",
    "description": "Log in to access Code Clinic events and schedules. Specify your role (student or volunteer) to determine access scope.",
}

logout = {
    "hint": "Disconnect from Google Calendar.",
    "description": "Disconnect from Google Calendar and remove access tokens. You will need to re-authenticate to access events and schedules.",
}


status = {
    "description": "Check if you're logged in and see the role (Student or Volunteer) you're logged in as",
    "hint": "View your current login status",
}


students = {
    "description": (
        "Access student-specific actions such as browsing available help sessions, "
        "booking, and managing your existing bookings.\n"
        "Use commands like 'student sessions' to see available sessions or 'student book' to reserve your spot."
    ),
    "hint": "Student commands to find and book help sessions",

    "sessions": {
        "description": (
            "View all upcoming help sessions offered by volunteers.\n"
            "Find a time that works for you and get the support you need."
        ),
        "hint": "List available help sessions you can join",
    },

    "bookings": {
        "description": (
            "See all the help sessions you’ve booked.\n"
            "Use this to review your upcoming appointments or manage your schedule."
        ),
        "hint": "List your current booked help sessions",
    },

    "book": {
        "description": (
            "Reserve a spot in an available help session.\n"
            "Select a session that fits your schedule and learning needs."
        ),
        "hint": "Book a help session",
    },

    "cancel": {
        "description": (
            "Cancel one of your existing bookings.\n"
            "This will free up the slot for other students."
        ),
        "hint": "Cancel a booked session",
    },
}



volunteers = {
    "description": (
        "Access volunteer-specific actions to create, view, and manage your help sessions.\n"
        "Use commands like 'volunteer create' to add a new session or 'volunteer slots' to view your available times."
    ),
    "hint": "Volunteer commands to manage help sessions",

    "slots": {
        "description": (
            "See your available time slots where you can offer help sessions.\n"
            "Helps you plan and offer support to students more effectively."
        ),
        "hint": "View your available time slots",
    },

    "sessions": {
        "description": (
            "View all help sessions you've created.\n"
            "Track your commitments and see which ones have been booked."
        ),
        "hint": "List your created help sessions",
    },

    "create": {
        "description": (
            "Create a new help session for students to book.\n"
            "You can specify the topic, time, and other details to guide students."
        ),
        "hint": "Create a new help session",
    },

    "cancel": {
        "description": (
            "Cancel one of your upcoming help sessions.\n"
            "Use this if your availability changes or the session is no longer needed."
        ),
        "hint": "Cancel a scheduled help session",
    },
}

