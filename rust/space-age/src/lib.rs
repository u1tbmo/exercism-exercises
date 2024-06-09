const EARTH_YEAR_IN_SECONDS: f64 = 31_557_600.0;

#[derive(Debug)]
pub struct Duration {
    seconds: u64,
}

impl From<u64> for Duration {
    fn from(s: u64) -> Self {
        Duration { seconds: s }
    }
}

pub trait Planet {
    fn orbital_period_relative_to_earth() -> f64;

    fn years_during(d: &Duration) -> f64 {
        d.seconds as f64 / (EARTH_YEAR_IN_SECONDS * Self::orbital_period_relative_to_earth())
    }
}

pub struct Mercury;
pub struct Venus;
pub struct Earth;
pub struct Mars;
pub struct Jupiter;
pub struct Saturn;
pub struct Uranus;
pub struct Neptune;

macro_rules! planet_impl {
    ($planet:ident, $period:expr) => {
        impl Planet for $planet {
            fn orbital_period_relative_to_earth() -> f64 {
                $period
            }
        }
    };
}

planet_impl!(Mercury, 0.240_846_7);
planet_impl!(Venus, 0.615_197_26);
planet_impl!(Earth, 1.0);
planet_impl!(Mars, 1.8808158);
planet_impl!(Jupiter, 11.862615);
planet_impl!(Saturn, 29.447498);
planet_impl!(Uranus, 84.016846);
planet_impl!(Neptune, 164.79132);
