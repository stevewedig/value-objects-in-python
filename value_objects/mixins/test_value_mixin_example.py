
import unittest

from value_objects import ValueMixin, Opt
from value_objects.util.testing import assert_equal_objects_and_strings, assert_unequal_objects_and_strings

# ============================================================================
# classes
# ============================================================================

class Image( ValueMixin ):
  def __init__( self, url, height = Opt.absent, width = Opt.absent ):
    pass

class Article( ValueMixin ):
  def __init__( self, url, title, image = Opt.absent ):
    pass

class Feed( ValueMixin ):
  def __init__( self, url, title, articles ):
    pass

# ============================================================================
# test
# ============================================================================

class ValueMixinTestCase( unittest.TestCase ):

  def test_value_mixin_example( self ):

    # same images
    image1 = Image( "http://image.com", Opt( 20 ), Opt( 30 ) )
    image2 = Image( "http://image.com", Opt( 20 ), Opt( 30 ) )
    assert_equal_objects_and_strings( image1, image2 )

    # image with different url
    assert_unequal_objects_and_strings( image1, Image( "http://xxx.com", Opt( 20 ), Opt( 30 ) ) )

    # image without size
    assert_unequal_objects_and_strings( image1, Image( "http://image.com" ) )

    # same articles
    article1 = Article( "http://article.com", "My Article", Opt( image1 ) )
    article2 = Article( "http://article.com", "My Article", Opt( image2 ) )
    assert_equal_objects_and_strings( article1, article2 )

    # article with different url
    assert_unequal_objects_and_strings( article1, Article( "http://xxx.com", "My Article", image1 ) )

    # article with different title
    assert_unequal_objects_and_strings( article1, Article( "http://article.com", "xxx",
        image1 ) )

    # article with different image
    assert_unequal_objects_and_strings( article1, Article( "http://article.com", "My Article", Image( "http://xxx.com" ) ) )

    # article without an image
    assert_unequal_objects_and_strings( article1, Article( "http://article.com", "My Article" ) )

    # same feeds
    article3 = Article( "http://article3.com", "My Article 3" )
    feed1 = Feed( "http://feed.com", "My Feed", ( article1, article3 ) )
    feed2 = Feed( "http://feed.com", "My Feed", ( article1, article3 ) )
    assert_equal_objects_and_strings( feed1, feed2 )

    # feed with different url
    assert_unequal_objects_and_strings( feed1, Feed( "http://xxx.com", "My Feed", (article1, article3) ) )

    # feed with different title
    assert_unequal_objects_and_strings( feed1, Feed( "http://feed.com", "xxx", (article1, article3) ) )

    # feed with different articles
    assert_unequal_objects_and_strings( feed1, Feed( "http://feed.com", "My Feed", (article1, ) ) )

    # feed with different article order
    assert_unequal_objects_and_strings( feed1, Feed( "http://feed.com", "My Feed", (article3, article1) ) )

    # feed without articles
    assert_unequal_objects_and_strings( feed1, Feed( "http://feed.com", "My Feed", tuple() ) )

  def test_comparison_to_non_value_objects( self ):

    image = Image( "http://image.com" )
    
    assert_unequal_objects_and_strings( image, 1 )
    
    assert_unequal_objects_and_strings( image, None )
    
    