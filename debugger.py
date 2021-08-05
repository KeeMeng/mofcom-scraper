from bs4 import BeautifulSoup

page = BeautifulSoup("""
<DIV class="art-con art-con-bottonmLine">
	<DIV align="center">
		<a href="http://english.mofcom.gov.cn/article/newsrelease/significantnews/202011/20201103012533.shtml" target="_blank"><img style="width: 100px;" src="/images/ev.gif" border="0"></a>
	</DIV>
	<p style="text-indent: 2em;"><p style="text-indent: 2em;">
		10月22日下午，商务部长钟山同德国联邦经济和能源部长阿尔特迈尔通电话，就落实中德欧领导人重要共识、深化中德和中欧经贸合作交换意见。
	</p>
	<p style="text-indent: 2em;">
		钟山表示，今年以来，习近平主席同默克尔总理三次通电话，共同出席中德欧领导人视频会晤，就加强抗疫合作、深化中德欧关系等达成一系列重要共识。新冠肺炎疫情发生后，中德守望相助、同舟共济，携手抗击疫情，加强宏观经济政策协调，为人员和货物跨境流动提供便利，推动双边经贸合作稳定健康发展。
	</p>
	<p style="text-indent: 2em;">
		钟山指出，当前全球疫情还在蔓延，世界经济面临严峻挑战。在习近平主席亲自指挥、亲自部署下，中国疫情防控取得重大战略成果，经济社会正常秩序基本恢复。中国正在加紧推动形成以国内大循环为主体、国内国际双循环相互促进的新发展格局，这将为包括德国在内的世界各国提供更广阔市场和发展机遇。中德作为各自所在地区重要经济体和重要经贸合作伙伴，要为国际抗疫和恢复经济注入更多正能量，促进经济全球化健康发展。为此，钟山建议，中德两国要继续加强抗疫合作，推动双边经贸务实合作提质升级，进一步充实中欧全面战略伙伴关系内涵。
	</p>
	<p style="text-indent: 2em;">
		阿尔特迈尔表示，德方对中国在疫情防控和经济发展方面取得的成就表示祝贺，感谢中方对德方抗击疫情提供的支持。德中在医疗物资贸易领域的良好合作，体现出稳定畅通的供应链和自由贸易的重要性。面对新的形势，德中和欧中需要加强沟通协调，加快推进中欧投资协定谈判，共同推动世贸组织改革，维护多边贸易体制，抵制单边主义和保护主义，为世界经济复苏作出积极贡献。
	</p>
	<p>
		(All information published on this website is authentic in Chinese. English is provided for reference only.)
	</p>
</DIV>
""", "html.parser")
# print(page.find("div", {"class": "art-title"}).get_text())

# def get_children(parent):
# 	children = []
# 	for child in parent.findChildren():
# 		print("==============")
# 		print(parent)
# 		print("---")
# 		print(child)
# 		print("---")
# 		if child.findChildren() == []:
# 			print("child get text")
# 			print(child.get_text())
# 			children.append(child.get_text())
# 		# else:
# 		# 	print("get children")
# 		# 	children.extend(get_children(child))
# 	return children

# content = page.find("div", {"class": "art-con-bottonmLine"})
# print(content.get_text())
# print("=================")
# print(content.find("img").findChildren())
# [print(str(i)+"\n\n") for i in content.findChildren()]
# print(get_children(content))

print(page.find("div"))


# zh_link = None
# for div in content.find_all("div"):
# 	if div.find("a"):
# 		zh_link = div.find("a")["href"]
# print(zh_link)