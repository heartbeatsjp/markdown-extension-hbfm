# -*- coding: utf-8 -*-

from hbfm.number_headers import NumberHeadersPreprocessor


class TestNumberHeaders():
    def setup(self):
        self.preprocessor = NumberHeadersPreprocessor()

    def test_crosslink(self):
        mdtext = u"""
## あり

[あり](#あり)

### をり

[をり](#をり)

#### はべり

[はべり](#はべり)

## いまそがり

[いまそがり](#いまそがり)
        """

        lines = self.preprocessor.run(mdtext.split("\n"))

        except_text = u"""
## 1. あり

[1. あり](#あり)

### 1.1. をり

[1.1. をり](#をり)

#### 1.1.1. はべり

[1.1.1. はべり](#はべり)

## 2. いまそがり

[2. いまそがり](#いまそがり)
        """

        assert "\n".join(lines) == except_text

    def test_deadlink(self):
        mdtext = u"""
## あり

[なし](#あり)
        """

        try:
            self.preprocessor.run(mdtext.split("\n"))
            assert False
        except KeyError as e:
            assert e.args[0] == u"なし"
            assert True
