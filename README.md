# Simulation_Modeling

This code is a Python program that simulates a queue or waiting line scenario using the Pygame library. The simulation involves customers arriving at a queue, waiting in line, and either entering a facility or exiting it based on a specified schedule. Here's an explanation of the code:

1. Importing Libraries:
   - The code starts by importing the necessary libraries:
     - `pygame` for creating the graphical simulation.
     - `random` for generating random numbers (not used in this code).
     - `time` for introducing delays.

2. Main Function:
   - The `main` function is defined to set up and run the simulation.

3. Configuration Variables:
   - The code sets several configuration variables:
     - `n` is the number of customers.
     - `t` is the total time for the simulation.
     - `customer` is a list of tuples, where each tuple represents a customer's arrival time and the type of action they perform (1 for entering, 2 for exiting).
   
4. Pygame Initialization:
   - Pygame is initialized, a window is created, and the window's title is set.

5. Color Definitions:
   - Three colors are defined for drawing the simulation:
     - `text_color` (white) for text.
     - `line_color` (red) for lines representing the queue.
     - `object_color` (green) for objects representing customers.

6. Queue and Time Line Drawing:
   - The code uses a loop to draw lines representing the queue and a time line.
   - It calculates the positions and spacing based on the number of customers and the total time.
   - Numbers are drawn along the queue and the time line.
   
7. Simulation Loop:
   - The simulation loop runs while updating the screen.
   - It iterates through positions on the queue and simulates customer arrivals and actions.
   - It keeps track of time and the number of customers in the queue.
   - It updates the display, introduces a small delay, and checks for a quit event (e.g., closing the window).

8. Customer Arrival and Action:
   - As the simulation progresses, customers arrive at the queue based on the schedule defined in the `customer` list.
   - The code adds customers to a queue (`q`) when their arrival time matches the current time.
   - The type of action (entering or exiting) is recorded for each customer in the queue.
   - The code also checks if any customers in the queue have completed their action and removes them.

9. Drawing Objects:
   - The code draws objects (customers) entering and exiting at the appropriate positions on the queue.
   - Customers entering are represented as green circles at the exit end of the queue, and customers exiting are represented as green circles at the entrance end of the queue.

10. Pygame Event Handling:
    - The code checks for quit events (closing the window) using `pygame.event.get()`.
    - If a quit event is detected, the Pygame window is closed, and the simulation terminates.

11. Pygame Cleanup:
    - After the simulation loop completes, Pygame is shut down using `pygame.quit()`.

12. Main Function Invocation:
    - The program's main function is invoked if the script is executed directly, ensuring that the simulation starts.

This code provides a simple visual representation of a queue where customers arrive and perform actions at specific times. The code draws the queue and updates it in real-time, allowing you to observe the progression of customers through the queue.
