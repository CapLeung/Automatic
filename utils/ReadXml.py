from xml.dom import minidom


class ReadXml(object):
    def read_xml(self, fileName, firstNode, secondNode):
        root = minidom.parse(fileName)
        firstNode = root.getElementsByTagName(firstNode)[0]
        secondNode = firstNode.getElementsByTagName(secondNode)[0].firstChild.data
        print(secondNode)
        return secondNode


if __name__ == '__main__':
    el = ReadXml()
    el.read_xml('../DataXml/data.xml', 'jia', 'num1')
    el.read_xml('../DataXml/data.xml', 'jia', 'num2')