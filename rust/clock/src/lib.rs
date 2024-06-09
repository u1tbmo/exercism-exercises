use core::fmt;

#[derive(Debug, PartialEq)]
pub struct Clock {
    hours: i32,
    minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        Clock { hours, minutes }.normalize()
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock {
            hours: self.hours,
            minutes: self.minutes + minutes,
        }
        .normalize()
    }

    fn normalize(self) -> Self {
        let mut hours = self.hours + self.minutes.div_euclid(60);
        let minutes = self.minutes.rem_euclid(60);
        hours = hours.rem_euclid(24);
        Clock { hours, minutes }
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:0>2}:{:0>2}", self.hours, self.minutes)
    }
}
