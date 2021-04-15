import unittest
from wikipedia_for_humans import *


class TestQuickQuestions(unittest.TestCase):
    """ these methods can more or less be plugged straight into a chatbot """
    def test_convenience(self):
        page = "mercury god"
        self.assertTrue(short_answer(page) == tldr(page) == short_summary(page))
        self.assertTrue(long_answer(page) == summary(page))

        query = "gaul"
        self.assertTrue(best_paragraph(query, page) == ask_about(query, page))
        self.assertTrue(best_sentence(query, page) == tldr_about(query, page))

    def test_summary(self):
        self.assertTrue(summary("dog").startswith("The domestic dog "))

    def test_search(self):
        self.assertEqual(ask_about("lifespan", "dog"),
                         "In 2013, a study found that mixed-breed dogs live on average 1.2 years longer than purebred dogs. Increasing body-weight was negatively correlated with longevity .The typical lifespan of dogs varies widely among breeds, but for most, the median longevity, the age at which half the dogs in a population have died and half are still alive, ranges from 10 to 13 years. Individual dogs may live well beyond the median age of their breed.")
        self.assertEqual(ask_about("wolf", "dog"),
                         "The generally accepted earliest dog remains were discovered in Bonn-Oberkassel, Germany. Contextual, isotopic, genetic, and morphological evidence shows that this dog was clearly not a local wolf. The dog was dated to 14,223 years ago and was found buried along with a man and a woman, all three being sprayed with red hematite powder and buried under large, thick basalt blocks. The dog had died of canine distemper. Earlier remains dating back to 30,000 years ago have been described as Paleolithic dogs but their status as dogs or wolves remains debated, because considerable morphological diversity existed among wolves during the Late Pleistocene.This timing indicates that the dog was the first species to be domesticated in the time of hunter–gatherers, which predates agriculture. DNA sequences show that all ancient and modern dogs share a common ancestry and descended from an ancient, extinct wolf population which was distinct from the modern wolf lineage. Most dogs form a sister group to the remains of a Late Pleistocene wolf found in the Kessleroch cave near Thayngen in the canton of Schaffhausen, Switzerland, which dates to 14,500 years ago. The most recent common ancestor of both is estimated to be from 32,100 years ago. This indicates that an extinct Late Pleistocene wolf may have been the ancestor of the dog, with the modern wolf being the dog's nearest living relative.The dog is a classic example of a domestic animal that likely traveled a commensal pathway into domestication. The questions of when and where dogs were first domesticated have taxed geneticists and archaeologists for decades. Genetic studies suggest a domestication process commencing over 25,000 years ago, in one or several wolf populations in either Europe, the high Arctic, or eastern Asia. In 2021, a literature review of the current evidence infers that the dog was domesticated in Siberia 23,000 years ago by ancient North Siberians, then later dispersed eastward into the Americas and westward across Eurasia.")

    def test_tldr(self):
        self.assertEqual(tldr_about("wolf", "dog"),
                         "A strategy has been reported in Russia where one wolf lures a dog into a heavy brush where another wolf waits in ambush.")
        self.assertEqual(tldr_about("speed", "cheetah"),
                         "Estimates of the maximum speed attained range from 80 to 128 km/h .")
        self.assertEqual(tldr_about("distance", "jupiter"),
                         "The average distance between Jupiter and the Sun is 778 million km and it completes an orbit every 11.86 years.")
        self.assertEqual( tldr_about("distance", "venus"),
                          "Venus orbits the Sun at an average distance of about 0.72 AU , and completes an orbit every 224.7 days.")
        self.assertEqual(tldr_about("distance sun", "mars"),
                         "Mars's average distance from the Sun is roughly 230 million km , and its orbital period is 687 days.")
        self.assertEqual(tldr_about("distance", "uranus"),
                         "Its average distance from the Sun is roughly 20 AU .")
        self.assertEqual(tldr_about("danger", "mercury"),
                         "Some facial creams contain dangerous levels of mercury.")
        self.assertEqual(tldr_about("gaul", "mercury god"),
                         "Visucius was worshiped primarily in the frontier area of the empire in Gaul and Germany.")