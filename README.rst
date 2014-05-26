NikolaHub
==========

Your Nikola blog rendered in the cloud.

.. warning::

   This is a *work in progress* (and a proof of concept)
   No functional code yet (and may be never)

How it (will) work(s)
---------------------

When you push something to your blog repo, Github tell it to NikolaHub via a `webhook <https://developer.github.com/webhooks/>`_. Then NikolaHub pulls your code, build your site with `Nikola <http://getnikola.com/>`_ and push back the output folder to the `github pages branch <http://pages.github.com/>`_.

So, you can edit your post online, using `the built-in Github editor <https://github.com/blog/905-edit-like-an-ace>`_ or something like `prose.io <https://github.com/prose/prose>`_, commit your changes and enjoy your updated blog after few seconds.
