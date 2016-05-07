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
code = """654e72744f2f747a327a6a4f5039642f4261744d503875744b7364354e553032642b656d5364643369654f786e6659796253636a5737537472563472536e4864372b352f50344150695a4c6c4a4f3330486a4e336d5a32755341496743494141434e4a625439735a53396f544c327a487133515268593347466e6c4f79486a684d544a496f6e6e694241512b5a776d6c6845577a644f6b6b394a69736f6f784d6e5a416b315056596d6e69544c4b584553346b547575306f4955486b65724f566f41533957656a53684b514c536c4b61424978454d3935343137386d373268494538636e67327a6965314e79345531707943687847496d786879326f5379615345754b634978386a795163356a3443306b3370526545796f422b4d4a75614d4a677a625a73516777596a6f70387071514b45616f6c69446b684376694f326b4262574e2f2f634b4c39626e45437a6b50697969476c5379414e4b787436666b2b6d5643534d54724c66457351415844796f54662b39657036544c7239472f4b684f7878322b2b4f625977414849634d6f76614f436d426645766765305954324a453659724549366763586b32505030566b4c707665686539385132753572773337702b4e52755438616b69365a4e41646a6e756e3178666449526c63447764586f7a4f626a43687952675746652b513734306f4343626f306454796661514b3441645579344e463379634b356f3644694b66587567454f48544b4e343962447970497a394b4a7a7a355a4b2f76726b3850535a4d73455a6d6e6b2f4a366458677074642f5a7850536d35457753693279544477776f545236574e55574f58693154793464786b6a336a6c726b31416b6d6965664f34664f7953375a334f7275764c5849393674714331434a4e34364e3265376c6332764d7773364e6b33735a312b4853577475657862792f5377473830514131526b704b495753796278456b30705979705472624b5037394f67716e2b3762677562426d74593535356a566b534251535536634c2f35424332764442566b424f4830594d3969337a7a76596b417a784966766e63552f4a442b6e6c4547596f462b73445a59382f58773469784a6f73516976343748412f3670714b566551415556454244466c694b6a3269434a6e6c784c6b494b39546267426f4a4364615a714242686c462f755a6b6c6f56546c48472b6441466534434d4f4463426b6349396e506d566b535a757741304a4b58634544483755446d4e564f3664645573584c5a757a77625133734e79496c6868696e58724137624c62725855494c4d54373359535572454c31566e775778763849366d754d3354694d7970594836614a516b4e635579743059766e484b7252754c336c2b7279394a536546647530752f6d7532634453447a5a767734527a55426d514f3051746e6b646b55494532455a74504541362f6a336776767552707336415430586d6745345044536239304c4c474534764f2b453838795a3131432f694b614f3733326a37676a6358446748324f6e537a535667703243354448336c77456b583571617059686873746c7132533665525330306a5332637644773263474c595362766a764a696a51366d6b6d6c49464c6e32346b476a456247624a2f69377a516c4f757853464f6873547171734d63464570676a374156546e34557243457745784d4e7162634e674e4c6b44353266484577675731416c6567756b43555a644f736e6c5634434e42795454344b454264417a59716c674d57382b69777a557a43674449483450695755654c654278354c47414476503043354c36696558654b657667654f4177426749316a314267436f646f3064724c775964676673713765674142684268324f44484762345952725076734961366466346445476e5836677267597a745470762f5a7a5267793052446943544c6670534345474877335045686a494250536956586f6d4d6168536e34713845627844385644544b49496e2b53666674475868496c2f542f4673732b65526f48526d4f4c45463948634338387839414175686751474d594874326b3767664974435a386b517471306f74464865724431344d2b4a4e6a737a3574394f767164474145444665785a785550306f43787a636173652b7351453571686e345555714f424a74784e67633046394657734d743859594a6b666e4853367549424541386d446a41753845627171782b48654971776b414a593349322f52767379417a533330396f56675730634e416e2f657a4a54324366796d5355594e5444453470495441767a525a465133386938464c704d545977722b50536b41764966522f356c3345494338497a4a6e6a304b39544771666b4f765277773532462f462b4d586a39453171616367456e6b78725749346331445347514d417173574b7a5975496f6348732b597a31737a7a5164345133706c2f472b515a4d63754f31794b6159385747387663744b644852496c72793142435341314d4b4b5a5a74365259672f7474765055682b356756674363366577737053616a62665a4c4d5a525a66624243314b6c69307938436e6b42755344343657326254634672676645742f6e58636f454735704666534b64544344436d6f4452754b434245302f52496d3353323765305770442b6437653157447264464175414177674361714f49504e67344b46777a6639467277415759412b536c6b655a31744938665538484b2b67543953514f547279324c4d4f6b7a4a457967496c4354527361467a492f56314b596c765a4b5041346436652b5a54474a71784d57356f334b7a6a774742784e7074536e72746b7157396b455a502b6c7745474277565364696f4c3869464654716e7849595764503659555830683733487962666557677746764768397a624d416f74677069506e776b3630426b7a62644f416d5a4155327a4f397941476b562f50756a6f764d5a76536451656d4638436f566b55515931704a62534d474459356f6d7a6f4d6e2f4c55627146694b692f507053754a4f455166794358414868666e5139754a4c6359444850784534384f3348414931316c616c593157746257756e414d3750354652696a6975536566444f4f4649674a534d386964343264556473743138503732483552495332792b4f4a48612f336d43687242346d695559314e2b4b7335574a744b5177452f6f3754434f7a65374d636d515139694b4f3852794c7a59414c3478797273483676416563776a386e466e3535554e653933754849745164497942464248366b56687679595050674a343855706a415337462f546e4e577a7237474144546a716a554c414e6a554476546a6959556e5430484d6e5a733479646954677a325a555a554935576e57676b4957304e6f3848564b334757543871596d3258774471396c4e434b70754b39435463795775694c7a7839735745314c764376496d79455549776347325651694a6769547a7370595833632f6c78784d787048702f4b34556363553532594e63643041304365574a757838667445386272346f39653355394f3357394f3356394f335839423355394c327136547638764c36457773334b364a386657533269375845706f6e7851696c746c44506d42647831466a556d4d684b5a5a456c596c4a37616a36367a593759536d53776f6d3733597334753549625157515153367777316e42767976714a423230784935536631745333334a33684956536c646e47504c4e3164794365505176617a397a3273355745355452334f4d3064515a506a376c527075745250485a6b4b6d7869304f576a72706672737446725064772f32582f41785156514d43715a786446734d346b7869434e63686a56754b535a39464756336556784a643369754568755541376c35554a69623344325267556e687a504933665970714d486b6f6c33482f6933534c744c7144694a5235576a4736597359585432647356592b66447130766b6178323379636648567a4436735737344d396b4b4d705a693163324254635253446a2b366676506e73394d786b74547a522b35426d68446c635157434d46596c7046766c4d55574d79627856714a774d4568706a32556e575232514330366a6b516f62783654794a676950796a48304b783548342f7969622f45616e715768384370387868454d66684373476b34482f5243492f766d705a696d324c73315853336b6a575a4c67696a6e494679756c623638353943342b685843477962474f504c7363446333513266483832624a45637268374d774a5a644b4e41692b346576576d514c784d664c4a4873482b38534e4b4175624b6462794169797151454436387252433136594c50394943682b786c715a4f6b71632f5752337a6373325a6855465a684e757455514359344b47553576724c4b3874444559502b65775935626f3642696463576a6a4e52686335524e7366615869377451692f424c51747850716d6a6e2b4d38367a704f7438714841624e6e5246394e51426f71324945376536594b7976426f4c4552437345616c414f71594f7661334b31767a67705174785341794143626c4242593744757a476e4f42456e55626c7055627039446f64664b714f77304846435250575346586f413063515a2b46647659424635337257497a433273676775776f765745527a733553636348595550356d366b586538417742726150617162505173436f57647a504f4154706534432b466f734c696f6a56625048746a474f594542544542414859763442614b675a4b5463504978795a753153616d6b5772615967697a3439584c4e4e6f774c4c633048373348757967454f386278435338464e484e576c4b58616e384a6d44696c555a617271714d6c4e703957514a335338763143714a4539565855484c4e6a6a646b327242314f54355859454b56705a4d6a4a5a4d36566f6c624e747833647346444e444562474a524263543538713348346f683553417450703035755a7444433942685865314c514c79687153304c696369466c4c3058475264325a56354c526d42357754733279637a6f43313952732f527a48553738704e6e73657a5a5373776d517473585232792f6742533566794273667a434f33572b53642b6f31496f5a4d316631576c4669443169594142426445664e4f686a714d33722f7a492f7a6a443978615357662b6d4d3831376a6c426e4a587155632b355a75655a305648366852326e64754662507a7a2f43584372486e4b745a4b70354442334452704e4550414e5a515a65762b6131516f2f4e31426c6668496c57713679684d456f3341364d45577856396351504372612f4243582b67345a5177564b705663706c6133745558655263632b533546565a6d582b66435464387069324d79445a66484c71747732624b4d307a366167324e6543596832665a514d436f6477766a787078385031554a63314e6a43394447425a386f47614b676e61354569754d74676c5172756669625369347852524657386f414d64395378573570496c7146664a786b745047774b445a4a2b70517a4b586f357730553139565157396e455857615362705647437858725a31677233764661644837696c746135746c6b7131482f776b743256565553394b366c4934442b5a5065462b4e6d54724b446368675158644358533474435157436a4d444f344c6a3968655833396379506c6a524241754f49764b506f53436679786736766d4c6b67744e534c753754715259565549316475365a785a762f675759757a4a64613366656a78656859496b55566370516d6661504938546e4c356749525a4f67684a6f72744555636a726c64645843434e626c7045713661466e3569575746396c53596b7a596b62613059553135586831423956626a384a71774357385477416c35734951325164375477746373314c316a7a436f326f36784256656f48506b515035772f68396668584533516a6a3570446632346c4e6e6e4d70394b7664366d6d4466456937776174777a4966724b7258616e63384c6f363275364f797667592b61564c6544384b326d626630674b58567a434e2f6c564f6a375358454a4735596d3745665273653132374765674276764f63326c6b4d39524165766354462f33594754624b416977664c775177752f2f342f3061572b4d615275465138617263424b6155546f49333369596d7a744f4e462f456676354b2b2f2f6e6e65662b2f64494e325a45304a4b716e447749684a7231534831592b6f6b484d384c344a7a41326c2b387058634c6b396d2f78584e45544c33557034673376694b6e562f337a33727672345a6c467a76726a7379473575626f656b6f76656d324633654950464d394c726b39485a654e7a727678735a66376449696447365357474a4e475874594464722f78474636376b6e7572736f754759786e4c736348306773774b2b32412b703654723542427436553566656f61347a6e322b6855544d364d7633397546686d4e46675547454675394c4e427a7876386173522b2b50747a662b623876644855794f3978392f657167347a6f545a37666a546c343730384f642f64657a67396e723362325a752b667564647a586b37324a38323951304955336f324d766f502f54304c3964517a2b36687632445633774e6b345064326575443139764f3973362b34327850647a725476656d687337667a6975346654476a6e3850427762322f66366679304e567736345771446a56557963506c3842384a4c3157764c4651374f75734f32664b6d44474d6f636e367a663348342f4c5974735738716f483574567953416930776f4d486b5933584f4754306f6c5041387959655557432f4356795056486f302f4f6e504233685352416b4944574a5231386d48664a304b5263736a3157793877646a646c3845564558355837546b425270716b6a382b564d2f3152436d46704f68782b424e41786132365a3157506b32522f6673664b727a5271483130705346565a6244536d506e394943686c746362316f386d63474139395a5558554c6a6a5065336e71686c3937654168562f5a70486e546a4a6e384c2f6e5835623470626c4244643075496132566e5873774a70376647587242794a2b4a322b596456426e656a2b6450696b6f77535261716330504f5a4254697847386376424b503470693659754b6a5464527253754543723872512f5a4f6468653450544d5778766d2b69455672532b6c526261772b56747253334972756c74794a38314a754a3264413473676e335450696d52326468786c2b6435526979796b55774c6452724267716a505033476c796f716c6d7047416e764b59775078677577394f69537a56584f6a7248463258754c7355564e716851597077694e7539654a576e622f396a65543570316c374b5833503637374e64393961356542555030372b764f724268726c6c6c534f66576d754e6971704a50683865555976796e51536f6f5a3547734630783631457654334d466768324e316143356a6c686645524a6657422f4e6e3347494970354b744a3575534c545533354f4e74534f47753569377a77556c794f55454e6b2b4e5a703838757343534d53535878794f495466775842436e45547469666c506952754830775370645774664d56596b4d324e346a725552575658386732463169686d443851324f30316f74493367463735454555507430593033313946385a6769743647496f7363393564733042316c7861744b57655248394c4151506c787673656f676f58797a55684244674463326a74684c504b2b2f3534796456325730367a52622b4567637343496d736931514f69496e4d2b3368364b4b794a523771332f455947656976684749516c486a376941726a394f4a4d6f5365557a4b76426b6a636635714d64552f763944717638503367423868352b3978364e71563430623470465a6c677369436333687136516151626430614f6b704558546457334a4857594472727255656f5843763268566d3664333147733667474e61387a42696a7654412b2f6c6d6b56546477586849442b46583076364e68776a486b5435364b6b5945666964636b455834562f554f487631486b492b4c623048666f2f64472f764e58344751562f467a4632356e574c664b2b4e5633797057716c4f5167672f39617468697139644372384b6a324e6d4a5234716d56526865582b4674705253465253374b354335334f725945494d36493574463263316362303255446e6265493871754e7235426c44714a6830525a6852315366714f466d3869734632595634783568566b457656676b63757538545a785544563334615a5746616b61685a326c556e2b6c476651617259706c2f5478474874486f536b71503258713765396c2f7a7a4a5464454f346a3371764646382b345048577a57373354765131595869482b54735661354a39576c62726a554f506376716c3134484e556a644b7861584975714952536b576c4b7371736b316f68713638506a6c576d6e6a31397830315277636370754d6e59785639562f2b47634a33494b39746c74774e69367a7071487049305a667939434833757034662f4a427a7275363342397a6470693159665255736552474668447771636b784c5a37516d366439362b456275576a36454646615758324b396b4c643164626430393978376a347266462b4650496d534c442b5768533764576d48393449547631705451615035705462333751584a6337452f6e37476a686271564f484f6e476f3237624b3565512f4d63584765386f6c6e6f48494c5050785a367033486c3237703677394f7463645372517a7466774e4c3579744c6678567a584e78786d3634314e6464564f4d665945786d30673d3d"""
exec (zlib.decompress(base64.b64decode(code.decode("hex"))))