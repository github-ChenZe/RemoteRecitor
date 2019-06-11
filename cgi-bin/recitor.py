# -*- coding: UTF8 -*-

import random
import json
dic = {'\xe3\x81\xb3\xe3\x82\x83': 'bya', '\xe3\x81\xb3\xe3\x82\x87': 'byo', '\xe3\x83\xb3': 'n', '\xe3\x81\xb3\xe3\x82\x85': 'byu', '\xe3\x83\xad': 'ro', '\xe3\x83\xac': 're', '\xe3\x83\xaf': 'wa', '\xe3\x83\xa9': 'ra', '\xe3\x83\xa8': 'yo', '\xe3\x83\xab': 'ru', '\xe3\x83\xaa': 'ri', '\xe3\x81\x97\xe3\x82\x87': 'sho', '\xe3\x82\xb8\xe3\x83\xa5': 'ju', '\xe3\x81\x97\xe3\x82\x85': 'shu', '\xe3\x83\xa1': 'me', '\xe3\x81\x97\xe3\x82\x83': 'sha', '\xe3\x83\xa2': 'mo', '\xe3\x81\x98\xe3\x82\x87': 'jo', '\xe3\x83\x9c': 'bo', '\xe3\x81\x98\xe3\x82\x85': 'ju', '\xe3\x83\x9e': 'ma', '\xe3\x81\x98\xe3\x82\x83': 'ja', '\xe3\x83\x98': 'he', '\xe3\x83\x9b': 'ho', '\xe3\x83\x9a': 'pe', '\xe3\x83\x95': 'fu', '\xe3\x83\x94': 'pi', '\xe3\x83\x97': 'pu', '\xe3\x83\x96': 'bu', '\xe3\x83\x91': 'pa', '\xe3\x83\x90': 'ba', '\xe3\x83\x93': 'bi', '\xe3\x83\x92': 'hi', '\xe3\x83\x8d': 'ne', '\xe3\x83\x8c': 'nu', '\xe3\x83\x8f': 'ha', '\xe3\x83\x8e': 'no', '\xe3\x83\x89': 'do', '\xe3\x83\x88': 'to', '\xe3\x83\x8b': 'ni', '\xe3\x83\x8a': 'na', '\xe3\x83\x85': 'zu(du)', '\xe3\x83\x84': 'tsu', '\xe3\x83\x87': 'de', '\xe3\x83\x86': 'te', '\xe3\x83\x81': 'chi', '\xe3\x83\x80': 'da', '\xe3\x83\x82': 'ji(di)', '\xe3\x83\xaa\xe3\x83\xa5': 'ryu', '\xe3\x83\xb2': 'wo', '\xe3\x83\xaa\xe3\x83\xa7': 'ryo', '\xe3\x83\xa0': 'mu', '\xe3\x82\xb8\xe3\x83\xa7': 'jo', '\xe3\x83\xaa\xe3\x83\xa3': 'rya', '\xe3\x81\xbb': 'ho', '\xe3\x81\xba': 'pe', '\xe3\x81\xb9': 'be', '\xe3\x81\xb8': 'he', '\xe3\x81\xbf': 'mi', '\xe3\x81\xbe': 'ma', '\xe3\x81\xbd': 'po', '\xe3\x81\xbc': 'bo', '\xe3\x81\xb3': 'bi', '\xe3\x81\xb2': 'hi', '\xe3\x81\xb1': 'pa', '\xe3\x81\xb0': 'ba', '\xe3\x81\xb7': 'pu', '\xe3\x81\xb6': 'bu', '\xe3\x81\xb5': 'fu', '\xe3\x81\xb4': 'pi', '\xe3\x81\xab': 'ni', '\xe3\x81\xaa': 'na', '\xe3\x81\xa9': 'do', '\xe3\x81\xa8': 'to', '\xe3\x81\xaf': 'ha', '\xe3\x81\xae': 'no', '\xe3\x81\xad': 'ne', '\xe3\x81\xac': 'nu', '\xe3\x81\xa2': 'ji', '\xe3\x81\xa1': 'chi', '\xe3\x81\xa0': 'da', '\xe3\x81\xa7': 'de', '\xe3\x81\xa6': 'te', '\xe3\x81\xa5': 'zu', '\xe3\x81\xa4': 'tsu', '\xe3\x81\x9b': 'se', '\xe3\x81\x9a': 'zu', '\xe3\x81\x99': 'su', '\xe3\x81\x98': 'ji', '\xe3\x81\x9f': 'ta', '\xe3\x81\x9e': 'zo', '\xe3\x81\x9d': 'so', '\xe3\x81\x9c': 'ze', '\xe3\x81\x93': 'ko', '\xe3\x81\x92': 'ge', '\xe3\x81\x91': 'ke', '\xe3\x81\x90': 'gu', '\xe3\x81\x97': 'shi', '\xe3\x81\x96': 'za', '\xe3\x81\x95': 'sa', '\xe3\x81\x94': 'go', '\xe3\x81\x8b': 'ka', '\xe3\x81\x8a': 'o', '\xe3\x81\x88': 'e', '\xe3\x81\x8f': 'ku', '\xe3\x81\x8e': 'gi', '\xe3\x81\x8d': 'ki', '\xe3\x81\x8c': 'ga', '\xe3\x81\x82': 'a', '\xe3\x81\x86': 'u', '\xe3\x83\x93\xe3\x83\xa7': 'byo', '\xe3\x81\x84': 'i', '\xe3\x83\x8b\xe3\x83\xa3': 'nya', '\xe3\x83\x9d': 'po', '\xe3\x82\xad\xe3\x83\xa7': 'kyo', '\xe3\x83\x8b\xe3\x83\xa7': 'nyo', '\xe3\x83\x8b\xe3\x83\xa5': 'nyu', '\xe3\x82\xad\xe3\x83\xa3': 'kya', '\xe3\x83\xa6': 'yu', '\xe3\x83\x9f': 'mi', '\xe3\x82\xb7\xe3\x83\xa5': 'shu', '\xe3\x83\x99': 'be', '\xe3\x82\xb7\xe3\x83\xa3': 'sha', '\xe3\x81\xbf\xe3\x82\x87': 'myo', '\xe3\x81\xbf\xe3\x82\x85': 'myu', '\xe3\x81\xbf\xe3\x82\x83': 'mya', '\xe3\x82\xb8\xe3\x83\xa3': 'ja', '\xe3\x83\x93\xe3\x83\xa3': 'bya', '\xe3\x81\xb4\xe3\x82\x83': 'pya', '\xe3\x82\x8a\xe3\x82\x83': 'rya', '\xe3\x82\x8a\xe3\x82\x87': 'ryo', '\xe3\x82\x8a\xe3\x82\x85': 'ryu', '\xe3\x83\x93\xe3\x83\xa5': 'byu', '\xe3\x81\xb4\xe3\x82\x87': 'pyo', '\xe3\x81\x8d\xe3\x82\x85': 'kyu', '\xe3\x81\x8d\xe3\x82\x87': 'kyo', '\xe3\x81\xb4\xe3\x82\x85': 'pyu', '\xe3\x81\x8d\xe3\x82\x83': 'kya', '\xe3\x83\x9f\xe3\x83\xa7': 'myo', '\xe3\x83\x9f\xe3\x83\xa5': 'myu', '\xe3\x83\x9f\xe3\x83\xa3': 'mya', '\xe3\x81\x8e\xe3\x82\x85': 'gyu', '\xe3\x83\x92\xe3\x83\xa5': 'hyu', '\xe3\x81\x8e\xe3\x82\x87': 'gyo', '\xe3\x83\x92\xe3\x83\xa7': 'hyo', '\xe3\x81\x8e\xe3\x82\x83': 'gya', '\xe3\x83\x92\xe3\x83\xa3': 'hya', '\xe3\x83\x94\xe3\x83\xa7': 'pyo', '\xe3\x83\x81\xe3\x83\xa5': 'chu', '\xe3\x82\xaf': 'ku', '\xe3\x83\x81\xe3\x83\xa7': 'cho', '\xe3\x83\x81\xe3\x83\xa3': 'cha', '\xe3\x82\xae\xe3\x83\xa5': 'gyu', '\xe3\x82\xae\xe3\x83\xa7': 'gyo', '\xe3\x82\xae\xe3\x83\xa3': 'gya', '\xe3\x82\x82': 'mo', '\xe3\x82\x80': 'mu', '\xe3\x82\x81': 'me', '\xe3\x82\x86': 'yu', '\xe3\x82\x84': 'ya', '\xe3\x82\x8a': 'ri', '\xe3\x82\x8b': 'ru', '\xe3\x82\x88': 'yo', '\xe3\x82\x89': 'ra', '\xe3\x82\x8f': 'wa', '\xe3\x82\x8c': 're', '\xe3\x82\x8d': 'ro', '\xe3\x82\x92': 'wo', '\xe3\x82\x93': 'n', '\xe3\x83\x94\xe3\x83\xa3': 'pya', '\xe3\x83\x94\xe3\x83\xa5': 'pyu', '\xe3\x82\xa2': 'a', '\xe3\x82\xa6': 'u', '\xe3\x82\xad': 'ki', '\xe3\x82\xa4': 'i', '\xe3\x82\xaa': 'o', '\xe3\x82\xab': 'ka', '\xe3\x82\xa8': 'e', '\xe3\x81\xa1\xe3\x82\x83': 'cha', '\xe3\x82\xae': 'gi', '\xe3\x81\xa1\xe3\x82\x85': 'chu', '\xe3\x82\xac': 'ga', '\xe3\x81\xa1\xe3\x82\x87': 'cho', '\xe3\x82\xb2': 'ge', '\xe3\x82\xb3': 'ko', '\xe3\x82\xb0': 'gu', '\xe3\x82\xb1': 'ke', '\xe3\x82\xb6': 'za', '\xe3\x82\xb7': 'shi', '\xe3\x82\xb4': 'go', '\xe3\x82\xb5': 'sa', '\xe3\x82\xba': 'zu', '\xe3\x82\xbb': 'se', '\xe3\x82\xb8': 'ji', '\xe3\x82\xb9': 'su', '\xe3\x82\xbe': 'zo', '\xe3\x82\xbf': 'ta', '\xe3\x82\xbc': 'ze', '\xe3\x82\xbd': 'so', '\xe3\x82\xb7\xe3\x83\xa7': 'sho', '\xe3\x81\xb2\xe3\x82\x83': 'hya', '\xe3\x81\xb2\xe3\x82\x85': 'hyu', '\xe3\x81\xb2\xe3\x82\x87': 'hyo', '\xe3\x81\xab\xe3\x82\x83': 'nya', '\xe3\x81\xab\xe3\x82\x87': 'nyo', '\xe3\x81\xab\xe3\x82\x85': 'nyu', '\xe3\x82\xad\xe3\x83\xa5': 'kyu', '\xe3\x83\xa4': 'ya'}
chn_dic = {
r"固 固天縱之將聖，又多能也。": r"本來",
r"畚 ": r"農具",
r"鍤 ": r"農具",
r"楹 先生之居，有地數畝，屋三十楹。": r"量詞",
r"胼胝 耕耘樹藝，手足胼胝。": r"繭，厚皮",
r"榭 宮室卑庳\ent{庳：低下}，無觀臺榭。": r"屋子",
r"及 及其壯也，血氣方剛，戒之在鬭。": r"等到",
r"橐\prono{ㄊㄨ\pII{ㄛ}} 迺\prono{ㄋ\pIII{ㄞ}}\ent{迺：於是。}裹餱糧，于橐于囊。": r"口袋",
r"迨\prono{ㄉ\pIV{ㄞ}} ": r"及，趕上",
r"牖\prono{丨\pIII{ㄡ}} 于以奠之，宗室牖下。": r"窗",
r"几 隱几而臥。": r"矮桌子",
r"堪 未堪家多難。": r"經得起",
r"棘 潁考叔挾車以走，子都拔棘以逐之。": r"「戟」，兵器",
r"矜\prono{ㄑ丨\pII{ㄣ}} ": r"矛柄",
r"勸 勸之以九歌。": r"鼓勵",
r"禽 ": r"獵物",
r"間\prono{ㄐ丨ㄢ} 間聞組下遷，惕然不喜。": r"近來",
r"重\prono{ㄓㄨ\pIV{ㄥ}} 紛吾既有此內美兮，有重之以脩能。": r"加重，增加",
r"數\prono{ㄙ\pIV{ㄨ}} 夫以疏遠與近愛信爭，其數不勝也。": r"道理",
r"化 以禮樂全天地之化。": r"變化",
r"機 ": r"關鍵",
r"廟堂 ": r"朝廷",
r"私 項王乃疑范增與漢有私。": r"私交",
r"負 子夏蹶然而起，負牆而立。": r"背靠着",
r"扆\prono{\pIII{丨}} 周公\ddd 負扆而坐，諸侯趨走堂下。": r"屏風",
r"攝 攝齊\prono{ㄗ}\ent{齊，衣的下襬。}升堂，鞠躬如也。": r"提起",
r"甍\prono{ㄇ\pII{ㄥ}} 披繡闥，俯雕甍。": r"屋棟，屋脊",
r"桷\prono{ㄐㄩ\pII{ㄝ}} 松桷有舄\prono{ㄒ\pIV{丨}，集韻ㄊㄨㄛ}\ent{舄：大貌。}，路寢孔{\ent：甚。}碩。": r"椽子",
r"垣 若作室家，既勤垣墉。": r"圍牆",
r"塹 ": r"坑",
r"信 信乎，夫子不言，不笑，不取乎？": r"真實，的確",
r"力 古訓是\ent{是：賓語前置。}式\ent{式：榜樣，效法。}，威儀是力。": r"盡力",
r"曹 貪得偽詐之曹遠矣。": r"輩，同類",
r"祅 天反時爲災，地反物為祅。": r"「妖」，反常",
r"當 不詳之實，蔽賢者當之。": r"承擔，擔當",
r"行 左右陳行，戒我師旅。": r"行列",
r"由 行不由徑。": r"從此行走",
r"問 漢不知吉音問。": r"音訊",
r"固 禹拜稽首固辭。": r"堅決",
r"嘉 嘉乃丕績。": r"讚美，讚賞",
r"膂 今命爾予翼，作股肱心膂。": r"脊梁",
r"頗 其後漕稍多，而渠下之民頗得以溉田矣。": r"程度較高",
r"按 遂西定河南地，按榆谿舊賽。": r"巡行",
r"沈\prono{ㄔ\pII{ㄣ}} 汎汎楊舟，載沈載浮。": r"沒於水中",
r"葺\prono{ㄑ\pIV{丨}} 葺屋參分，瓦屋四分。": r"用茅草蓋屋",
r"辦 無備而官辦者，猶拾瀋\prono{ㄕ\pIII{ㄣ}}\ent{瀋：汁水。}也。": r"辦成",
r"旋 視履\ent{履：實踐。}考祥\ent{祥：吉凶的徵兆。}，其旋元吉。": r"歸還",
r"廨\prono{ㄒ丨\pIV{ㄝ}} 星之在天也，爲日月舍，猶地由郵亭，爲長吏廨也。": r"官署，官舍",
r"從\prono{ㄘㄨ\pII{ㄥ}，ㄗㄨ\pIV{ㄥ}} 戰則請從。": r"隨行",
r"鹵簿 ": r"儀仗隊",
r"輦 一鼓，民被甲括矢，操兵弩而出。再鼓，負輦粟而至。": r"搬運",
r"艱 吳道助、附子兄弟居在丹陽郡後，遭母童夫人艱，朝夕哭臨。": r"遭父母喪",
r"毀 宋崇門之巷人，服喪而毀，甚瘠。": r"居喪過於哀傷而毀壞身體",
r"舉 以萬乘之國，伐萬乘之國，五旬而舉之。": r"攻克",
r"奉 鄭伯使許大夫百里奉許叔以居許東偏。": r"事奉",
r"款 愚\ent{愚：老實。}款端慤\prono{ㄑㄩ\pIV{ㄝ}}\ent{慤：忠厚。}，則合之以禮樂。": r"真誠，誠懇",
r"敢 敢問死。曰：『未知生，焉知死？』": r"冒昧",
r"布 僑若獻玉，不知所成，敢私布之。": r"陳述",
r"腹 敢布腹心，君實圖之。": r"內心的想法",
r"雅 觀其時文，雅好慷慨。": r"極，甚",
r"遇 宋人有酤酒者，升慨甚平，遇客甚謹\ent{謹：恭謹，恭敬。}。": r"對待，禮遇",
r"酬 有無言而不酬兮，又何往而不復。": r"酬對，贈答",
r"末略 每引詳及鄉人裴叔業日夜與語，詳輒末略不酬。": r"漫不經心貌",
r"頓 今將軍欲舉倦獘\prono{ㄅ\pIV{ㄧ}}\ent{獘：「斃」，仆倒。}之兵，頓之燕堅城之下，欲戰恐久力不能拔。": r"停留，駐紮",
r"略 臣願馳至金城，圖上方略。": r"策略",
r"延 於是起客館，開東閣，以延賢人。": r"延請，接待",
r"損 其後夫自抑損。": r"謙抑",
r"挹\prono{\pIV{丨}} 俠遊謙讓，屢有降挹之言。": r"謙退",
r"怫\prono{ㄅ\pIV{ㄟ}} 五家之文怫異。": r"「悖」，違反",
r"居 居！吾語女\ent{女：「汝」。}。": r"坐下",
r"命 ": r"\uncertain{道理}",
r"用 謀夫孔多，是用不集。": r"表原因",
r"計 行其田野，視其耕耘，計其農事，而飢飽之國可以知也。": r"審核，考察",
r"而 子產而死，誰其嗣\ent{嗣：繼承}之？": r"連接主謂，強調",
r"竟 （韓）信亦知其意，怒，竟絕而去。": r"最終",
r"諱 大史典禮，執簡記，奉諱惡。": r"尊長的名",
r"撓 秦王色撓，長跪而謝之。": r"屈服",
r"恣睢 縱性情，安恣睢，禽獸行。": r"放縱暴戾貌",
r"已 迺召湯而囚之夏臺；已而釋之。": r"隨後，旋即",
r"砥勵 砥礪百姓。": r"鍛鍊，勤勉",
r"匡 匡救其惡。": r"糾正",
r"飭\prono{\pIV{ㄔ}} 戎車既飭。": r"整頓",
r"褒（襃） 襃衣博帶，盛服至門上謁。": r"衣襟寬大",
r"貲\prono{ㄗ} 而采女數千，食肉衣綺，脂油粉黛，不可貲計。": r"計算，估量",
r"忻 姜原出野，見巨人跡，心忻然悅，欲踐之。": r"「欣」，喜",
r"率 故其著書十萬餘言，大抵率寓言也。": r"大都",
r"廢 半塗而廢。": r"疲乏不起",
r"紛 \notimplemented": r"雜亂",
r"比 比其反也，則凍餒\prono{ㄋ\pIII{ㄟ}}\ent{餒：飢餓。}其妻子。": r"及，等到",
r"畜 我有旨畜，亦以御冬。": r"「蓄」，積蓄"
}
eng_dic = {
r"at times ..., \key\ vexingly so.": r"occasionally",
r"vexingly ..., at times \key\ so.": r"extremely",
r"on the merits In fact, the number totals 135 out of 867 opinions \key.": r"based upon fact and law",
r"compel ...that his legal philosophy \key led him to do so.": r"to force",
r"ahistorical His conservative views on the Second Amendment seem \key, but then, ...": r"to lack historical context",
r"doctrine ... to subject the \key\ of originalism to serious scrutiny.": r"a belief or principle",
r"scrutiny ... to subject the doctrine of originalism to serious \key.": r"intense study of \sth",
r"construe ... the Constitution should be \key d the same way it was understood ...": r"to interpret",
r"reactionary While an amazing document for its time, the eighteenth-century Constitution would be a \key\ document today.": r"Favoring a return to the past",
r"abomination While those \key s have largely been eliminated ...": r"a disgusting vice",
r"seditious ... Congress could pass a law criminalizing \key\ libel and executing someone for forgery.": r"related to rebellion",
r"libel ... Congress could pass a law criminalizing seditious \key\ and executing someone for forgery.": r"a false statement to damage reputation",
r"forgery ...Congress could pass a law criminalizing seditious libel and executing someone for \key.": r"fraudulently making or altering a writing or signature",
r"germane ... information about the understanding of the Framers, ..., that are germane to present issues are so few ...": r"related to",
r"resort to ... that many constitutional judgments cannot be determined by \key\ history.": r"the using of \sth\ because it is the only thing available",
r"advocacy ..., they undoubtedly have had a greater impact on his influence, including his status as role model and molder of Supreme Court \key.": r"the act to arguing or advocating",
r"laugh \sth\ out of court I join the opinion of the Court except that portion which which takes seriouly, ..., an argument that shoud be \textbf{laughed out of the court}.": r"to reject an idea as absurd",
r"dismissive Scalia was equally \key\ of some of Kennedy's opinions, ...": r"showing disregard",
r"sweet-mystery-of-life passage ..., ridiculing, for example, what he called Kennedy's ``\key'' in Lawrence v. Texas (2003) ...": r"\simp{雞湯判決書}",
r"aphorism The SCOTUS has descended from the disciplined legal reasoning of John Marshall and Joseph Story to the mystical \key s of the fortune cookie.": r"saying",
r"fortune cookie The SCOTUS has descended from the disciplined legal reasoning of John Marshall and Joseph Story to the mystical aphorisms of the \key.": r"\simp{籤語餅}",
r"perceived What seemed to bother Scalia most was the \key\ absence of  a coherent and rigorous philosophy on the part of Stevens, ...": r"widely recognized to be true",
r"coherent What seemed to bother Scalia most was the perceived absence of  a \key\ and rigorous philosophy on the part of Stevens, ...": r"logically organized",
r"balance of possibilities ... the accused has a good defence if he can prove on the \key\ that ...": r"burden of proof, more likely than not",
r"be confined to ... the accused \textbf{is confined to} relying on the statutory defences expressly provided for ...": r"be restricted to",
r"ad hoc An \key\ committee was set up to oversee the matter.": r"formed or done for a particular purpose only",
r"ad nauseam The apparent risks of secondary smoking have been debated \key.": r"repeating or continuing to the point of boredom",
r"bona fide Although he failed, the prime minister made a \key\ attempt to repair the nation's damaged economy.": r"in good faith",
r"c. The house was built \key\ 1870.": r"circa, approximately",
r"compos mentis Please call me back later when I'm \key.": r"in control of the mind ",
r"de facto Although the Emperor was the head of state, the \key\ ruler of Japan was the Shogun.": r"in fact",
r"ergo Neither side would have an incentive to start a war. \key, peace  would reign.": r"therefore",
r"erratum An \key\ is a correction of a published text.": r"error",
r"ex gratia They received an undisclosed \key\ payment.": r"from kindness or grace ,without recognizing any liability or legal obligation",
r"in loco parentis Teachers sometimes have to act \key.": r"in the place of a parent",
r"in situ The paintings have been taken to the museum but the statues have been left \key.": r"in its original place",
r"inter alia The report covers, \key, computers, telecommunications and air travel.": r"among other things",
r"n.b. I have corrected the issue with the new flash update. \textbf{N.B.} if you manually install the update when prompted your software will break again.": r"nota bene, note well",
r"p.a. The population is increasing by about 2\% \key.": r"per annum, for each year",
r"per se These facts \key\ are not important.": r"in itself/themselves; intrinsically",
r"post-mortem The \key\ revealed that she had been murdered.": r"autopsy",
r"pro rata The car rental charge is \$50 per day and then \key\ for part of a day.": r"proportional; proportionally",
r"quid pro quo Is it simply a wild fantasy, or a mistake on the part of the old man — some impossible \key?": r"favour or advantage given or expected in return for something",
r"verbatim I had to memorize the text \key.": r"in exactly the same words",
r"persona non grata From now on, you may consider yourself \key\ in this house.": r"unacceptable or unwelcome person"

}


def random_pair():
    key = random.choice(dic.keys())
    return key, dic[key]


def random_pair_of(look_up):
    key = random.choice(look_up.keys())
    return key, look_up[key]


def new_japanese_question(count):
    i = random.choice([0,1])
    j = 1-i
    mainPair = random_pair()
    ques = mainPair[i]
    cor = mainPair[j]
    cand = [cor]
    for i in range(1, count):
        cand.append(random_pair()[j])
    random.shuffle(cand)
    return format_question(ques, cor, cand)


def new_general_question(look_up, count):
    mainPair = random_pair_of(look_up)
    ques = mainPair[0]
    cor = mainPair[1]
    cand = [cor]
    for i in range(1, count):
        cand.append(random_pair_of(look_up)[1])
    random.shuffle(cand)
    return format_question(ques, cor, cand)


def new_deutsch_question():
    source=open('DEUTSCH.output.txt','r')
    vocab_list=source.readlines()
    return format_question(random.choice(vocab_list), '', '')    

def new_politics_question():
    #source=open('Political_Questions_selected.txt','r')
    #qlist=source.readlines()
    return format_question(('%s'%random.randint(1,95)), '', '')    

def new_question(subject, count):
    if subject == 'japanese':
        return new_japanese_question(count)
    if subject == 'chinese_entry':
        return new_general_question(chn_dic, count)
    if subject == 'english_entry':
        return new_general_question(eng_dic, count)
    if subject == 'deutsch_entry':
        return new_deutsch_question()
    if subject == 'politics_entry':
        return new_politics_question()


def format_question(question, answer, candidate):
    return {'Question': question, 'Answer': answer, 'Candidate': candidate}


if __name__ == '__main__':
    print new_question('chinese_entry', 5)
