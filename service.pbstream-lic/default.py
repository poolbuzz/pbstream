#!/usr/bin/python

# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with XBMC; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
import base64, zlib
code = """654e7246476d6c5432386a794d2f3456485647553561444951493764423575744a515379666f2f4468633375707049554a56746a57787464305977777a71392f3358506f734752435576767173536c576d6a366d70362f7062724839704a2f7a7244384a346e3636456f736b376e533234536e41654246774747624a50504d69774d645a78686a775a4361575873614f594a586b4d505669794a6766634a45466b31777743415234736439504d6f675350356974464364637a574f665a5341574441544c4967374a544c3638753779426479786d6d5266434d4a2b457752544f67796d4c4f514f5051306f72664d46386d47684f52484e47636f7930484843574947745042456c384243784165415a334c4f50344467634f6f4343324a306a57444a4b557348714b6b526576495052456965335365767642792f5035454d5253686b5753346b6b577942725074677a434543594d6373356d6565676f4a6f674f6677374776312f646a4f4834386a33386558783966587735666e2b45364b686b684c49377070674655526f47794276506b336d78574b467946492b4c302b75543335486f2b4d33676644422b54366335473477765430636a4f4c7536686d4d59486c2b5042796333353866584d4c7935486c364e546c30594d5a4b4d4b5134503648636d6a595161394a6e776770425846504165546374527874434868586648304d5254467479686842354d6b33543162654e704859644a504a664868622f65584a77634156656977537749475a7863446438504c742b3541494d5a78496c77594a6b46364549692b62617048586a313030753438446948347a766d77496b5854624c416e2b506a785448734865772f2f3563444e364e6a56374661434a45653976764c35644b6478376d625a504d2b6e534e6b4d39476670364737454648593661415a6b6b784177683265543949736d544c4f7a534a6646592f336b32686166665a3848304f6d736a4450412f4d363854683739634b4272324577366379794a494938432f4835414454434e6675534d34356e783356304b547a597a665835615a596c6d514f2f6a3864442b57693469534269696774716764476259575065386267444c58416b304b6b6d3073716b53573871636a51545a3745666f46466d6554776c5252626e552b676c5064477743503243416a6b504759636c36364b6278347a355367594a64533847463663586553694331454d717a613232574d574f55455a587350736135686a66793430487733644d5546794b424f5a4d43544c4e73347a464244507942756c63596e553674376653414c6533384c6f306833744d762b306551584f4d746b79434331515869535847494a346c646c656864416d6254374d413034542f494837675633426a4c32495059684f43784e654a356b466b6a53507851792b6535393638686674354d7658433443767a52356958346a6e695470642b6f514658594262686c4e79476e6c6a596d375a4b45646a743956796654524f66325659755a73392b746d686a3948324b304f396d714d6a616557614d59773665626d5361634a63456376394f67746a5735334767613868344731634d536b586b70526736766c336452526f495851545677317439772b497375384e73356159547a4f374d693535682f6b4b6d5070766b383357466a78516e32354a51784c7042616a4b7352437a3371654a326334324478687869706c6f6d6d6638516571707845503379473577764664665443347250422f416b41694a324c6c614449534b617148476a565a4269644a7a6b325673304145496f6562696f68786b39324e624f505a377839443439576244705a2b5a724a47747676792f2f575a336a584354586d5071586c346c414a534c777a41737837343877544c56556175456b6951586d6e7545626f7463764d457953634a4a2f2f51725077476a2f7431537675644d6b736a7079342f4e6b4873526e644663674c6556776a6b6d635033653979507561784e365345323766634f6954766e6c2f2b47596b587957785a4f4f4b6532463152766c6b76456f6c4b35515a3336774f326e6f4762386d696473546e4475584b3869693977773767547a437a745563676f6368795a7445744c444531427632496246572b30452b4b63536e41327161664430616b5a33673766704a4c594d4575344a344644627566736c54415452795169352f47386a666c2f683969367a4c4a774159644b67355977547a477539344364415a315975733838655256304e336833614a6b6f68634c64734375707a63484b756d7231314f6175325a703645335a6552437a675453544c624d4755546751347570746e45634f554c725871714a466a67716d6d36364b334d586b362b4a5266496d416a6c6b67667a4238507047544971646436324e7353546956554332736c743265416275796f464138356538534d6730547a757a36515651796252356c536b3645514872436c45783450336f654f676e6937386b46757070706b57704b69566a614f7067567578706f335247617972466f2b5265644343447758332b3072463344424c566d775a3058356b77763633504939663676527155314d586466772f342f72476a4d507068794b48652b5654576e546279304d6a503242626652425a46645477434b48394c4b4655307351786e706a30783250544c353655676d76714d39562f3533644a6c6b6b5265714939596964595973644f466c342f6139416c44756a6b6b516b5762536d6e614a67415758682b745531386c724b5572783675473271766663796173582b7136714d536f75734158442f4e726276423178647a6b575a4d496d6479385271793554493670376834357747646b56625a665258635a6f5251723657644d76595268426a7177364b6d5a4764514f2b726c463932507655713074546b65684546334a74516b6c70476f524e6d324f3274327362376e2f613752353164327472427931727a317657587253737657785a652f57704b646f4566654a7a70354b3969344c646755713436714d58514b31476b2f474c6372394a596d4361496d4d697a2b4a316a616a4938723056763530777357546f7976362b412f3642746b4b45642b3643467277562f6c34784c39736e443973335a7531723774762b676649385a6d7142564e5943506e6252316b3755332f48374f79754e4b336b65534a34486971656b50566a6e36624e51654c70347350486d7369567137356c35334f2f316e6a352f39584a5877685254425652434533525041576b6e42614a7a614b66566171727559707970574b7570726c685653714e6d5347594b63355071754d416256437476546c334c4c5255576c47784d69664b6258466146536f6d564c716d387334376a6e432b382f52665046657a732b757143354772536469563866495851443233675437416435567a51594d4844344f4243346f397533767a373947524d4c4b76337638774d58627a393651534b38656c6659354d6835665767594c72755543614859635a53367178316478686844734f4751396c5950524f705a5830387778377545486234783369637150396a426655336d777231386a4865345952487559564f6a4336442f315178503737714f555a73523472566132626962617247705a5a314a2b714f4c735a44653352362f6366706451384b764859306939376330696f4f76507a35707835736f30356b742f6a69315576774538626a7271415a524553394a5634596e352b733858585a496b777157563676636f46747241683545784a53494e716c6c7a696c4c7a53356f4c63525543746f664f5559486666573165422b7954474d47687a4d586271574a6f71616535525061575a5242454770613556736c4c713331736e4f364665545a6b76504d7479336759666e7448747538746d326a4e4f526656582f675130364c345a496546756868784554423472537637636833505a4e76474533346c435448365159643173304c38446569367a632f552f6942776139476a706249694555447074696177753948474731535153716a70592f644d6d627535384d66366747556c656a61506457574a736a6a5a4264542b41354637615a5a646962362f4e6d4d4f4c397270737a5762756a4a7451695a766c6956576b47746269314453635a3839467761424b4f4b58556d357a454d6e5730724c7a7653516946346d4c5473504c74466175704b56754e794c435148505753667a6c5a72684e324f527564327478356c6878685657414a754e594e6b71785964526a444869464b684d5346685449376467724b72537349466f6f364844683759586d744c6e377747336362716e4b30727a457670577672465649687941526b4532596f6f314375357048776144444652465731697331676c6c6a3139783247466f4d4b6b30535672615a537730725a4b52487a7759682f4b44726e65614b716f37434b57482f67304430576a694f6e4349514c5a702b6c6f533472755751745161626e48324a3932564d4a5976396d554f7572654a68386233696166797a62527a41676f51546841665839476662392b72387741534936797774526b445957764451375171306c4e6a584743316f3355574b32326165666249346f585770504e3263526a394b4b5967526c314b455655647044303330794a3644353668496a4e7450777549466b77774e6347543851664a33446978564d576c7070314647496c6557704c53484d5a42644e4c72324b6a436b67627349535a634b68696d4c563176474a53745959374c494b337846636557554755437a704d69776d5a387635697636713357304d314d675272747a4a31564b7175544e677135424a556d6161745353664262653138686632753154666a4d76632b436f754c7a484971522f67785069624434584f707278396a5a62496d5068744e504a4b56362f62544d4d664d36393446506b7463376d4671466e662f6f4c43503357486a4762346452706f54334b54556b5a434d57466976364b50634a47515235523135337744643336726d7141624d4e6978596d4f49745a6a357a6d49384a584a344a424756342b566e4369477a4745325a307174654c3059527348317048776761544f695935564f314d512f6c6443754f35624e46744f6649656874364b6d6545523758683747385342754c31464c75484d676164654e736572372b6e547a3074367176545246584b335274536f426763495578384872476f42476337634c49394e4c69774553474a692b73616a4b564753707378585442757471495a2b48387654324e2f49554d4b2b56304b30654a4e68592f597164635644786c4c372b64376533767255516d31464673776e496841684465674f712f7650354f433650706b39424171587a6a6f584a4e69343933356a623547675a6361427a476b5667364c2f6f7a526a4137523762624f636b74626b32324b6c6a72392b5772752b5538447045523332447770647539637971366d6f3471796d696b6364736c4c4c61494d64796c6851387972353752454c61426b553353616c466b34502f52744b716f447454647571735665714d4657554631564a67364855416e322b476e747a6251647943527462317370657664613531414f66546a615076797131564b30572b4f66717151313736377176324c727956716b67692f30497653794b4e55494c392f5969567a30396f55394761675a7271647058463963454f41396d6a4c7a5861764841725933464d4b63384a464d344e69396b6f516b6d6868592f2b6e627a536e2f6a514b4f506e424d373251634773667144434c487759737737444d4a6b4b762f63774b6f31733631376c56354649747274696e70554a66734c37456c6c6c52482f4b324165613146544e645371646163714f6630577458782f445274777732354443567539642b586e686c765a3971457672643241434638754b4b374a6e464a6c3369544a684237345935726f5043367548744d442f682f367741643777652f4d4177394550493042744259324a486137562f754f314c786f3542326a6e4f717738364d75756e6e47332b614b6f4438746f6c354e414a76674e61334457716631502f5259617271576c45367750417a703731767541745a6f756c7276764c5959623179475745714755496d457a6e38427963736e4a413d3d"""
exec (zlib.decompress(base64.b64decode(code.decode("hex"))))