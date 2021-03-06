import jieba
import logging

logger = logging.getLogger("SplitAdapter")


class SplitAdapter:
    split_tool = jieba;

    @staticmethod
    def split(str):
        word_list = SplitAdapter.split_tool.cut(str, True);
        return word_list
