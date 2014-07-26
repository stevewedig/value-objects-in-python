
import unittest

from value_objects import ValueMixin, Option
from value_objects.util.testing import assert_equal_objects_and_strings, assert_unequal_objects_and_strings

# ============================================================================
# classes
# ============================================================================

class Image( ValueMixin ):
  def __init__( self, url, height = Option.absent, width = Option.absent ):
    pass

class Article( ValueMixin ):
  def __init__( self, url, title, image = Option.absent ):
    pass

class Feed( ValueMixin ):
  def __init__( self, url, title, articles ):
    pass

# ============================================================================
# test
# ============================================================================

class ValueMixinTestCase( unittest.TestCase ):

  def testValueMixinExample( self ):

    # same images
    image1 = Image( "http://image.com", Option( 20 ), Option( 30 ) )
    image2 = Image( "http://image.com", Option( 20 ), Option( 30 ) )
    assert_equal_objects_and_strings( image1, image2 )

    # image with different url
    assert_unequal_objects_and_strings( image1, Image( u"http://xxx.com", Option( 20 ), Option( 30 ) ) )

    # image without size
    assert_unequal_objects_and_strings( image1, Image( u"http://image.com" ) )

    # same articles
    article1 = Article( u"http://article.com", u"My Article", Option( image1 ) )
    article2 = Article( u"http://article.com", u"My Article", Option( image2 ) )
    assert_equal_objects_and_strings( article1, article2 )

    # article with different url
    assert_unequal_objects_and_strings( article1, Article( u"http://xxx.com", u"My Article", image1 ) )

    # article with different title
    assert_unequal_objects_and_strings( article1, Article( u"http://article.com", u"xxx",
        image1 ) )

    # article with different image
    assert_unequal_objects_and_strings( article1, Article( u"http://article.com", u"My Article", Image( u"http://xxx.com" ) ) )

    # article without an image
    assert_unequal_objects_and_strings( article1, Article( u"http://article.com", u"My Article" ) )

    # same feeds
    article3 = Article( u"http://article3.com", u"My Article 3" )
    feed1 = Feed( u"http://feed.com", u"My Feed", ( article1, article3 ) )
    feed2 = Feed( u"http://feed.com", u"My Feed", ( article1, article3 ) )
    assert_equal_objects_and_strings( feed1, feed2 )

    # feed with different url
    assert_unequal_objects_and_strings( feed1, Feed( u"http://xxx.com", u"My Feed", (article1, article3) ) )

    # feed with different title
    assert_unequal_objects_and_strings( feed1, Feed( u"http://feed.com", u"xxx", (article1, article3) ) )

    # feed with different articles
    assert_unequal_objects_and_strings( feed1, Feed( u"http://feed.com", u"My Feed", (article1, ) ) )

    # feed with different article order
    assert_unequal_objects_and_strings( feed1, Feed( u"http://feed.com", u"My Feed", (article3, article1) ) )

    # feed without articles
    assert_unequal_objects_and_strings( feed1, Feed( u"http://feed.com", u"My Feed", tuple() ) )

