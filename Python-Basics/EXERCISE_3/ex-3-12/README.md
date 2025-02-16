This script refactors earlier schedules to use the `Schedule` named tuple.
- This improves code readability and structure.
- Each stop is now an instance of `Schedule(time, station)`.
