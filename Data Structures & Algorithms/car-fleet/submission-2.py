class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        fleets = 0
        last_time = 0.0
        for p, s in pair:
            t = (target - p) / s
            if t > last_time:
                fleets += 1
                last_time = t
        return fleets