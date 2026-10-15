# Code Clinic Booking System

<div align='center'>

by [Poelano Ditshego](https://gitlab.wethinkco.de/poditshcjc025),
[Queen Mphahlele](https://gitlab.wethinkco.de/qumphahcjc025),
[Surpise Ramatsie](https://gitlab.wethinkco.de/suramatcjc025),
[Sizwe Khomo](https://gitlab.wethinkco.de/sikhomocjc025)

</div>


## Table of Contents

- [Summary](#summary)
    - [Quickstart: Installation & Usage](#quickstart-installation--usage)
- [Development Approach](#development-approach)
- [Requirements Gathering](#requirements-gathering)
    - [System Vision: Understanding the System](#system-vision-understanding-the-system)
    - [Use Cases: Understanding the User](#use-cases-understanding-the-user)
    - [Interaction Flow: Connecting the Dots](#interaction-flow-connecting-the-dots)
- [Functional Definition](#functional-definition)
    - [System Architecture: Drawing out the Blueprint](#system-architecture-drawing-out-the-blueprint)
    - [Components Mapping: Laying Down the Building Blocks](#components-mapping-laying-down-the-building-blocks)
    


## Summary

Our goal is to develop a command-line based platform that enables students to book help sessions with more experienced peers. The system will provide the following features:

- Google Calendar integration: Interacting with Google Calendar API to retrieve and update calendar data
- Data Storage: Securely storing configuration data and calendar information client-side
- Volunteer Management: Enabling students to volunteer for available time slots
- Booking Management: Allowing students to book help sessions with available volunteers
- Command-line interface: Providing a user-friendly interface for students to interact with the system

### Quickstart: Installation & Usage

To install the Code Clinic Booking System:
- Navigate to the ***build/*** directory
- Locate the ***install.sh***
- *Right-Click*, Go to **Properties/Permissions**
- Mark **"Allow executing file as program"**.
- *Right-Click*, **Run as Program**

After installation is complete, you can open a terminal and launch the tool by typing: `clinic`


## Development Approach

The Code Clinic Booking System will be a greenfield project, developed organically using an Agile methodology. This approach will allow us to iteratively design, develop, test, and refine the system throughout the project. By embracing an Agile mindset, we will be able to respond quickly to changing requirements, deliver working software in short cycles, and continuously improve the system.


## Requirements Gathering

Before we can design the solution, we need to have a comprehensive understanding of the nature of the system as a whole by performing analysis activities. As part of these activities, we are to produce the following key deliverables:

- System Vision: Outlining the overall goals, requirements, and capabilities of the system.
- Use Cases: Defining the system's functionality from the different users' perspectives.
- Interaction Flow: Mapping the roadmap through the system for the different users.

### System Vision: Understanding the System

To ensure a solid foundation for the system, we've created a document that accurately outlines the problem our solution addresses, ensuring a shared understanding of the system's purpose and functionality, while also acknowledging the system's boundaries, clearly defining what it will achieve and what it won't.

Our development process will be guided by the goals and constraints we have outlined, keeping us focused on delivering a solution that wholistically meets the specification.

*View the Full Document Here: [Beta Team - System Vision](docs/system-vision.pdf)* 

### Use Cases: Understanding the User

Now that we have an understanding of the system from a functional lens, we switch our focus to the interactions with the potential user. We have identified two different actors, the *Volunteer* and the *Student*, for which we have drafted Use Cases that outline how they are to interact with the system.

These use cases capture the system capabilities from the users' perspectives, enabling us to design a solution that meets their needs and expectations

*View the Full Document Here: [Beta Team - Use Cases](docs/use-cases.pdf)*

### Interaction Flow: Connecting the Dots

Now that we have a clear understanding of both the system and its users, we venture into uncovering how these two components interact by drafting flow diagrams. These diagrams visualize the key processes between users and the system’s various features, serving as a roadmap that details the user's journey.

This ensures the system facilitates a seamless and intuitive user experience, helping us refine the user interface and interactions.

*View the Full Document Here: [Beta Team - Flow Diagrams](docs/flow-diagrams.pdf)* 


## Functional Definition

Before we can build the system, we need to clearly define how it will function by breaking down its key components and their interactions. As part of this process, we produce the following essential deliverables:

- System Architecture: Outlining the high-level structure of the overall system.
- Component Mapping: Shaping the modular structure of the sub-systems.

### System Architecture: Drawing out the Blueprint

The system architecture offers a high-level view of the Code Clinic booking system, showing how core components—such as volunteer management, booking management, and the command-line interface-interact with each other and with the external services such as the Google Calendar API.

This blueprint establishes clear boundaries between responsibilities, supporting a system that is scalable, maintainable, and ready for future enhancements.

*View the Full Document Here: [Beta Team - System Architecture](docs/system-architecture.pdf)*


### Components Mapping: Laying Down the Building Blocks

While the system architecture gives us a bird’s-eye view of the system as a whole, component mapping zooms in to define the internal structure. It outlines major packages, groups related functionalities, and sets clear boundaries between them.

Identifying these building blocks early improves organization, simplifies maintenance, supports collaboration, and makes future scaling and refactoring easier.

*View the Full Document Here: [Beta Team - Components Mapping](docs/components-mapping.pdf)* 