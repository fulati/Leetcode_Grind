class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse = True)

        for p, s in cars: 
        
            travel = (target - p) / s

            if not stack or stack[-1] < travel: 
                stack.append(travel)
        
        return len(stack)