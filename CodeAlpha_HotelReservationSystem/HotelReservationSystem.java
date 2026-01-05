import java.util.*;

class Room {
    enum RoomType { STANDARD, DELUXE, SUITE }

    int roomNumber;
    RoomType type;
    boolean isBooked;

    public Room(int roomNumber, RoomType type) {
        this.roomNumber = roomNumber;
        this.type = type;
        this.isBooked = false;
    }

    public void bookRoom() {
        if (isBooked) {
            System.out.println("Room " + roomNumber + " is already booked.");
        } else {
            isBooked = true;
            System.out.println("Room " + roomNumber + " booked successfully.");
        }
    }

    public void cancelBooking() {
        if (!isBooked) {
            System.out.println("Room " + roomNumber + " is not booked.");
        } else {
            isBooked = false;
            System.out.println("Booking for room " + roomNumber + " cancelled.");
        }
    }

    @Override
    public String toString() {
        return "Room " + roomNumber + " (" + type + ") - " + (isBooked ? "Booked" : "Available");
    }
}

class Hotel {
    List<Room> rooms = new ArrayList<>();

    public Hotel() {
        // Add some rooms
        rooms.add(new Room(101, Room.RoomType.STANDARD));
        rooms.add(new Room(102, Room.RoomType.DELUXE));
        rooms.add(new Room(103, Room.RoomType.SUITE));
    }

    public void showRooms() {
        System.out.println("Rooms:");
        for (Room room : rooms) {
            System.out.println(room);
        }
    }

    public void bookRoom(int roomNumber) {
        for (Room room : rooms) {
            if (room.roomNumber == roomNumber) {
                room.bookRoom();
                return;
            }
        }
        System.out.println("Room number " + roomNumber + " not found.");
    }

    public void cancelBooking(int roomNumber) {
        for (Room room : rooms) {
            if (room.roomNumber == roomNumber) {
                room.cancelBooking();
                return;
            }
        }
        System.out.println("Room number " + roomNumber + " not found.");
    }
}

public class HotelReservationSystem {
    public static void main(String[] args) {
        Hotel hotel = new Hotel();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            hotel.showRooms();
            System.out.println("Enter room number to book, 'c' + room number to cancel, or 'exit' to quit:");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("exit")) break;

            if (input.startsWith("c")) {
                try {
                    int roomNumber = Integer.parseInt(input.substring(1));
                    hotel.cancelBooking(roomNumber);
                } catch (NumberFormatException e) {
                    System.out.println("Invalid input.");
                }
            } else {
                try {
                    int roomNumber = Integer.parseInt(input);
                    hotel.bookRoom(roomNumber);
                } catch (NumberFormatException e) {
                    System.out.println("Invalid input.");
                }
            }
        }
        scanner.close();
    }
}
