class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys_to_rooms = {0}
        room = [0]
        
        for r in room:
            for key in rooms[r]:
                room += [key] if key not in keys_to_rooms else []
                keys_to_rooms |= {key}
                    
        return len(keys_to_rooms) == len(rooms)