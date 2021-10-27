import unittest

from src.CleanText.clean_data import clean_text

BOOK_INTRO = """Neither Dale Carnegie nor the publishers, Simon and Schuster, anticipated more than this modest sale. 
 To their amazement, the book became an overnight sensation, and edition after edition rolled off the presses to keep 
 up with the increasing public demand.  How to Win Friends and Influence People  took its place in publishing history 
 as one of the all-time international best-sellers.  It touched a nerve and filled a human need that was more than a 
 faddish phenomenon of post-Depression days, as evidenced by its continued and uninterrupted sales into the eighties, 
 almost half a century later. \n Dale Carnegie used to say that it was easier to make a million dollars than to put a 
 phrase into the English language.  How to Win Friends and Influence People  became such a phrase:  quoted, 
 paraphrased, parodied; used in innumerable contexts, from political cartoons to novels.  The book itself was 
 translated into almost every known written language.  Each generation has discovered it anew and has found it 
 relevant. \n Which brings us to the logical question:  Why revise a book that has proven and continues to prove its 
 vigorous and universal appeal?  Why tamper with success? \n To answer that, we must realize that Dale Carnegie 
 himself was a tireless reviser of his own work during his lifetime.  How to Win Friends and Influence People  was 
 written to be used as a textbook for his courses in Effective Speaking and Human Relations and is still used in 
 those courses today.  Until his death in 1955 he constantly improved and revised the course itself to make it 
 applicable to the evolving needs of an ever-growing public.  No one was more sensitive to the changing currents of 
 present-day life than Dale Carnegie.  He constantly improved and refined his methods of teaching; he updated his 
 book on effective speaking several times.  Had he lived longer, he himself would have revised  How to Win Friends 
 and Influence People  to better reflect the changes that have taken place in the world since the thirties. \n Many 
 of the names of prominent people in the book, well known at the time of first publication, are no longer recognized 
 by many of today’s readers. """


class TestCleanText(unittest.TestCase):

    def test_clean_text_basic(self):
        self.assertEqual(clean_text("This is some basic test."), ['basic', 'test'])

    def test_clean_book_intro(self):
        self.assertEqual(clean_text(BOOK_INTRO), ['Neither',
                                                  'Dale',
                                                  'Carnegie',
                                                  'publisher',
                                                  'Simon',
                                                  'Schuster',
                                                  'anticipated',
                                                  'modest',
                                                  'sale',
                                                  'amazement',
                                                  'book',
                                                  'became',
                                                  'overnight',
                                                  'sensation',
                                                  'edition',
                                                  'edition',
                                                  'rolled',
                                                  'press',
                                                  'keep',
                                                  'increasing',
                                                  'public',
                                                  'demand',
                                                  'Win',
                                                  'Friends',
                                                  'Influence',
                                                  'People',
                                                  'took',
                                                  'place',
                                                  'publishing',
                                                  'history',
                                                  'one',
                                                  'time',
                                                  'international',
                                                  'best',
                                                  'seller',
                                                  'touched',
                                                  'nerve',
                                                  'filled',
                                                  'human',
                                                  'need',
                                                  'faddish',
                                                  'phenomenon',
                                                  'post',
                                                  'Depression',
                                                  'day',
                                                  'evidenced',
                                                  'continued',
                                                  'uninterrupted',
                                                  'sale',
                                                  'eighty',
                                                  'almost',
                                                  'half',
                                                  'century',
                                                  'later',
                                                  'Dale',
                                                  'Carnegie',
                                                  'used',
                                                  'say',
                                                  'easier',
                                                  'make',
                                                  'million',
                                                  'dollar',
                                                  'put',
                                                  'phrase',
                                                  'English',
                                                  'language',
                                                  'Win',
                                                  'Friends',
                                                  'Influence',
                                                  'People',
                                                  'became',
                                                  'phrase',
                                                  'quoted',
                                                  'paraphrased',
                                                  'parodied',
                                                  'used',
                                                  'innumerable',
                                                  'context',
                                                  'political',
                                                  'cartoon',
                                                  'novel',
                                                  'book',
                                                  'translated',
                                                  'almost',
                                                  'every',
                                                  'known',
                                                  'written',
                                                  'language',
                                                  'generation',
                                                  'discovered',
                                                  'anew',
                                                  'found',
                                                  'relevant',
                                                  'brings',
                                                  'u',
                                                  'logical',
                                                  'question',
                                                  'revise',
                                                  'book',
                                                  'proven',
                                                  'continues',
                                                  'prove',
                                                  'vigorous',
                                                  'universal',
                                                  'appeal',
                                                  'tamper',
                                                  'success',
                                                  'answer',
                                                  'must',
                                                  'realize',
                                                  'Dale',
                                                  'Carnegie',
                                                  'tireless',
                                                  'reviser',
                                                  'work',
                                                  'lifetime',
                                                  'Win',
                                                  'Friends',
                                                  'Influence',
                                                  'People',
                                                  'written',
                                                  'used',
                                                  'textbook',
                                                  'course',
                                                  'Effective',
                                                  'Speaking',
                                                  'Human',
                                                  'Relations',
                                                  'still',
                                                  'used',
                                                  'course',
                                                  'today',
                                                  'death',
                                                  'constantly',
                                                  'improved',
                                                  'revised',
                                                  'course',
                                                  'make',
                                                  'applicable',
                                                  'evolving',
                                                  'need',
                                                  'ever',
                                                  'growing',
                                                  'public',
                                                  'one',
                                                  'sensitive',
                                                  'changing',
                                                  'current',
                                                  'present',
                                                  'day',
                                                  'life',
                                                  'Dale',
                                                  'Carnegie',
                                                  'constantly',
                                                  'improved',
                                                  'refined',
                                                  'method',
                                                  'teaching',
                                                  'updated',
                                                  'book',
                                                  'effective',
                                                  'speaking',
                                                  'several',
                                                  'time',
                                                  'lived',
                                                  'longer',
                                                  'would',
                                                  'revised',
                                                  'Win',
                                                  'Friends',
                                                  'Influence',
                                                  'People',
                                                  'better',
                                                  'reflect',
                                                  'change',
                                                  'taken',
                                                  'place',
                                                  'world',
                                                  'since',
                                                  'thirty',
                                                  'Many',
                                                  'name',
                                                  'prominent',
                                                  'people',
                                                  'book',
                                                  'well',
                                                  'known',
                                                  'time',
                                                  'first',
                                                  'publication',
                                                  'longer',
                                                  'recognized',
                                                  'many',
                                                  'today',
                                                  'reader'])


if __name__ == '__main__':
    unittest.main()