import java.util.HashSet;
import java.util.List;
import java.util.Set;

class GottaSnatchEmAll {

    static Set<String> newCollection(List<String> cards) {
        Set<String> cardSet = new HashSet<>();
        for (String card : cards) {
            cardSet.add(card);
        }
        return cardSet;
    }

    static boolean addCard(String card, Set<String> collection) {
        return collection.add(card);
    }

    static boolean canTrade(Set<String> myCollection, Set<String> theirCollection) {
        boolean aHasTrade = false;
        boolean bHasTrade = false;

        for (String card : myCollection) {
            if (!theirCollection.contains(card)) {
                aHasTrade = true;
            }
        }

        for (String card : theirCollection) {
            if (!myCollection.contains(card)) {
                bHasTrade = true;
            }
        }

        return aHasTrade && bHasTrade;
    }

    static Set<String> commonCards(List<Set<String>> collections) {
        Set<String> common = new HashSet<>(collections.get(0));
        for (int i = 1; i < collections.size(); i++) {
            common.retainAll(collections.get(i));
            if (common.isEmpty()) {
                break;
            }
        }
        return common;
    }

    static Set<String> allCards(List<Set<String>> collections) {
        Set<String> all = new HashSet<>();
        for (Set<String> collection : collections) {
            all.addAll(collection);
        }
        return all;
    }
}
