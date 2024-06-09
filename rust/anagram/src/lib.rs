use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    let lower_word = word.to_lowercase();
    let sorted_word = sort_string(&lower_word);

    possible_anagrams
        .iter()
        .filter(|&&candidate| {
            let lower_candidate = candidate.to_lowercase();
            let sorted_candidate = sort_string(&lower_candidate);
            lower_word != lower_candidate && sorted_word == sorted_candidate
        })
        .copied()
        .collect()
}

fn sort_string(s: &str) -> Vec<char> {
    let mut chars: Vec<char> = s.chars().collect();
    chars.sort_unstable();
    chars
}
