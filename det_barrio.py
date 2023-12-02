# -*- coding: utf-8 -*-
"""Det_Barrio

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PGEhNxKcInIngNInboxaSbtzQaX86caV
"""

#Se importan las librerias
from shapely.geometry import Point, Polygon
import ast
import pandas as pd
import numpy as np

#Se lee el archivo barrios.csv
Barrios=pd.read_csv('barrios.csv',delimiter=';',encoding='latin-1', quotechar='\'', quoting=0)

#Se corrige uno de los datos

Barrios.iloc[40,0]="[(-58.3519574994471,-34.5981671240108),(-58.3517870396762,-34.5983816252281),(-58.3516310903926,-34.5985293578335),(-58.3515242372837,-34.5986294333382),(-58.3513250376732,-34.5987652009485),(-58.351151777729,-34.5989153023462),(-58.3509439264975,-34.5990486762005),(-58.3508486866856,-34.5990915201383),(-58.3506639992369,-34.5991581322739),(-58.3505831282684,-34.5992391508627),(-58.3504907597415,-34.5992915371235),(-58.3504535967438,-34.59933933799),(-58.3503202863848,-34.5995108066672),(-58.3503001077744,-34.5995261757045),(-58.3502076817729,-34.5995965662053),(-58.3500083112886,-34.5998563546356),(-58.3498726037683,-34.59996117245),(-58.3497310697798,-34.6001089159106),(-58.3495520771247,-34.6002280036794),(-58.3493442762458,-34.6003208288461),(-58.3487724661738,-34.6008354714777),(-58.3486079597807,-34.6009044845338),(-58.3484925616355,-34.6009210721909),(-58.3483350072205,-34.6009969594726),(-58.3481815929263,-34.6010784411798),(-58.3480326100217,-34.6011653625536),(-58.3478883399819,-34.601257558911),(-58.3477490544868,-34.601354856546),(-58.3476150186948,-34.6014570709298),(-58.3474864846987,-34.6015640085075),(-58.3473636969758,-34.6016754676043),(-58.3472468869406,-34.6017912357159),(-58.3471872596609,-34.6018558496398),(-58.3471628444741,-34.6018823054838),(-58.3471362762067,-34.6019110958216),(-58.3470320744147,-34.6020348200719),(-58.3469344781376,-34.6021621733931),(-58.3468436719653,-34.602292917094),(-58.3467598285131,-34.6024268025556),(-58.3467449976324,-34.6027201519366),(-58.3467146231891,-34.6027512327308),(-58.3466539441083,-34.6028133213455),(-58.3466496088104,-34.6028655503739),(-58.3467043639678,-34.6029013788664),(-58.3467214651499,-34.6030492694574),(-58.3466549069785,-34.6032042352505),(-58.3466404084886,-34.6032590787062),(-58.3465824730079,-34.6034355186902),(-58.346625528342,-34.6035882044085),(-58.3465618896651,-34.6037169373515),(-58.3465327462289,-34.6039315654346),(-58.3465412895755,-34.6040102811532),(-58.3464660230682,-34.6042034001614),(-58.3464745741156,-34.604277345459),(-58.3463877429124,-34.6044895342097),(-58.3463587041066,-34.6046278399618),(-58.3463152405234,-34.6047685180613),(-58.3462376213714,-34.6048115869957),(-58.3461737453739,-34.6048780956713),(-58.3460726192386,-34.6049972525663),(-58.3460897697303,-34.605109367729),(-58.3461415847436,-34.6051857386919),(-58.3461297903094,-34.6053693781153),(-58.3461672262755,-34.6054147302439),(-58.3461524904784,-34.6056389127914),(-58.3461176758174,-34.6057819833702),(-58.3461087048936,-34.6060085566211),(-58.3460826176215,-34.6060991644168),(-58.3460621519723,-34.6062947197848),(-58.3459580000821,-34.6065140472389),(-58.3458740789696,-34.6067047723038),(-58.3457382525162,-34.606883522391),(-58.3456198056659,-34.6070098170028),(-58.3452012257159,-34.6072312259671),(-58.345105898547,-34.6073265372621),(-58.3449239855223,-34.6074551552154),(-58.3447738879879,-34.6075241769181),(-58.344600635192,-34.6076480332287),(-58.3439973258681,-34.607943196189),(-58.343604538107,-34.6082767225298),(-58.3434486240146,-34.6083767428797),(-58.3432205247186,-34.6085243939173),(-58.3430530292876,-34.6086530240691),(-58.3426775424294,-34.6089865643439),(-58.3426238070897,-34.609029879918),(-58.3424233949318,-34.6091914297464),(-58.3422046890479,-34.6093637254023),(-58.3420191428825,-34.6094653137912),(-58.3417158385255,-34.6097488356722),(-58.3414646925724,-34.6098702249965),(-58.3412797619717,-34.610082312378),(-58.3412247682241,-34.6102086657767),(-58.340860627879,-34.6106638502637),(-58.3408631643594,-34.6109023595814),(-58.3408428246569,-34.6110025127638),(-58.3407876518246,-34.6112505043623),(-58.3407557628412,-34.6113577998157),(-58.3405819128756,-34.6118799557476),(-58.3404428739864,-34.6122685825448),(-58.3403618124167,-34.6124640769064),(-58.3402978502955,-34.6128026920278),(-58.3402309104948,-34.6132033159905),(-58.3400513710297,-34.6136658377204),(-58.3399760642656,-34.6138708775057),(-58.339935033596,-34.6143073036508),(-58.3399375499515,-34.6145577379736),(-58.3398591978443,-34.614870102752),(-58.3398445206534,-34.615041812305),(-58.3398445010592,-34.615663433595),(-58.3398553797087,-34.6161118369957),(-58.3399907003311,-34.6162956235298),(-58.3401289954027,-34.6164197853558),(-58.3405208604336,-34.6167517027698),(-58.3406683567111,-34.6168623326645),(-58.3407589856403,-34.616902353464),(-58.3408537609218,-34.6169381911497),(-58.3409510415291,-34.6169691012878),(-58.3410504525327,-34.6169949645084),(-58.3411516135194,-34.6170156821704),(-58.3412541331429,-34.6170311745533),(-58.3413576167572,-34.6170413808645),(-58.3415408599245,-34.6170571074179),(-58.3417246682417,-34.6170673904617),(-58.3419088039908,-34.6170722162365),(-58.3420930305336,-34.6170715781965),(-58.3422771101308,-34.6170654770082),(-58.3424608072124,-34.6170539214544),(-58.3425485917712,-34.617063368495),(-58.3426351674544,-34.6170786429924),(-58.3427199685172,-34.6170996452342),(-58.34280244235,-34.6171262394652),(-58.3428820505726,-34.6171582502818),(-58.3429582722951,-34.6171954698472),(-58.3430306117536,-34.617237655194),(-58.3432599856318,-34.6173124750228),(-58.3434923143504,-34.6173807826022),(-58.343727326471,-34.617442498324),(-58.3445624702041,-34.6176856322516),(-58.3446351482835,-34.6177043957661),(-58.3447096018188,-34.6177175702255),(-58.3447852028944,-34.6177250423396),(-58.3448613147964,-34.6177267510947),(-58.3449372942047,-34.6177226805444),(-58.3450125031783,-34.6177128661311),(-58.3450863048026,-34.6176973892731),(-58.3451580795391,-34.6176763818876),(-58.3452272197817,-34.6176500209767),(-58.3452783918189,-34.6176087581602),(-58.3453352229003,-34.617572912109),(-58.345396878145,-34.6175430102563),(-58.3454624552015,-34.6175194889261),(-58.3455309896949,-34.6175026960431),(-58.3456014781458,-34.6174928758306),(-58.3456728855952,-34.617490173326),(-58.3457372379493,-34.6175125727185),(-58.3458041205572,-34.6175291484966),(-58.3458727649543,-34.6175397097162),(-58.3459423829488,-34.6175441357286),(-58.3460121742565,-34.617542375286),(-58.3460813363111,-34.6175344492554),(-58.346133414209,-34.6175382463127),(-58.346184269818,-34.6175482675233),(-58.3462328217894,-34.6175642982151),(-58.3462780347429,-34.6175859984616),(-58.3463189487014,-34.6176129067147),(-58.3463645371003,-34.6176390775268),(-58.3464142137068,-34.6176595397951),(-58.3464669410637,-34.6176738661452),(-58.3465216161118,-34.6176817553434),(-58.3465770963436,-34.6176830440403),(-58.3466322205247,-34.6176777049882),(-58.3466858381327,-34.617665848872),(-58.3467368268049,-34.6176477243255),(-58.3467841206991,-34.6176237107469),(-58.3468267301346,-34.6175943093022),(-58.3468748443002,-34.6175825957114),(-58.3469197968922,-34.6175642039395),(-58.3469602437879,-34.6175396834947),(-58.3469949758198,-34.6175097688092),(-58.3470229537047,-34.6174753531307),(-58.3470433396935,-34.6174374678181),(-58.347049600361,-34.6174117430562),(-58.3470247401015,-34.6173839299003),(-58.3470882243088,-34.6173901658438),(-58.3471343101987,-34.6173737420078),(-58.3471779084981,-34.6173552569103),(-58.3472563135846,-34.6173369877322),(-58.3472914270823,-34.6173046926196),(-58.3474170487023,-34.6172762321474),(-58.3474930051357,-34.6172465789237),(-58.3475316708684,-34.6172135578311),(-58.3476039190031,-34.6171837784413),(-58.3476046629408,-34.6171661830377),(-58.347637388269,-34.6171489269963),(-58.3477182137283,-34.6171156129695),(-58.3478077427292,-34.61704652984),(-58.3479174269928,-34.6170060872261),(-58.3479981920537,-34.6170157040292),(-58.3481136234996,-34.6169919613083),(-58.3482175143644,-34.6169682085501),(-58.348292578981,-34.6169277331054),(-58.3483906831149,-34.6169158990191),(-58.348531273704,-34.6169287130293),(-58.3485637776474,-34.616918446296),(-58.3486474474023,-34.6169137541275),(-58.3487397399292,-34.6169329211544),(-58.3488522424976,-34.6169401818255),(-58.3489129180448,-34.6168734561617),(-58.349065881638,-34.6168282824533),(-58.3491445973469,-34.6168823024192),(-58.3492302835328,-34.6169606460598),(-58.3495851790084,-34.6170392395503),(-58.3497448447391,-34.6171029768609),(-58.349809918226,-34.6171103739143),(-58.3498547428776,-34.6171512064406),(-58.3499429749007,-34.6171618583073),(-58.3499784522252,-34.6171790112389),(-58.3500464355072,-34.6172230976539),(-58.350215088713,-34.6172036866238),(-58.3502653438831,-34.6172306364236),(-58.350268098694,-34.6173822755663),(-58.3502964750492,-34.6174184548607),(-58.3503448843904,-34.6174801759672),(-58.3505104109212,-34.6175854956796),(-58.3505812543603,-34.6177029562146),(-58.3505574000878,-34.6178423419497),(-58.3506015781976,-34.6179891279297),(-58.3506694967444,-34.6180821287572),(-58.3508096352105,-34.6181719461161),(-58.3503528758008,-34.6181356436174),(-58.350145636161,-34.6182479567702),(-58.3500450707419,-34.618233189407),(-58.3499209134411,-34.6181621485128),(-58.3497936303098,-34.618215836811),(-58.3498614742271,-34.6183626449496),(-58.3499117112203,-34.6184042685088),(-58.3499826537005,-34.6184483576873),(-58.3501009467587,-34.6184802616077),(-58.3501156201438,-34.6185683223673),(-58.3499717598301,-34.6186417181452),(-58.349967497668,-34.6187173756407),(-58.3502484649191,-34.6187787787067),(-58.3503373848246,-34.6186541275372),(-58.3504084002102,-34.6186444105033),(-58.3505298537621,-34.6185271259501),(-58.3507221173672,-34.6185517604431),(-58.3506865144456,-34.6186275451425),(-58.3505444343985,-34.6186836671394),(-58.350511637962,-34.6187245938928),(-58.3503966317689,-34.6188417743837),(-58.3503695487443,-34.6189354180379),(-58.3504404589871,-34.6190039647763),(-58.3505676569514,-34.6190231057418),(-58.3506651352135,-34.6191264579115),(-58.3506769091041,-34.6191704923281),(-58.3508248243659,-34.6191755201799),(-58.3511256372164,-34.6193060041146),(-58.3512119772248,-34.6193128952304),(-58.3512256172925,-34.6193127589578),(-58.3512257939416,-34.6193127564149),(-58.3512662181644,-34.6193122317506),(-58.3513194646905,-34.6193115402956),(-58.3513264575839,-34.6193114493246),(-58.3513385558446,-34.6193112927016),(-58.3513387619937,-34.6193112460149),(-58.351466913486,-34.6192822888025),(-58.3515015777937,-34.6192313593221),(-58.3515200778185,-34.6191674154407),(-58.3515411177224,-34.6191817152199),(-58.3515517787569,-34.6191889607893),(-58.3515861008513,-34.6192122870573),(-58.3516133025271,-34.6192307742144),(-58.3515633610247,-34.6193100292665),(-58.3515513017918,-34.6193291684615),(-58.3514630362213,-34.619359766701),(-58.3516495408997,-34.6194674630349),(-58.3516716626549,-34.6194800735768),(-58.3516836545812,-34.6194869101906),(-58.3517806687512,-34.619542216117),(-58.3519168318026,-34.6196198429122),(-58.3519171793806,-34.6196200406431),(-58.3519769433949,-34.6196226955548),(-58.3521671727199,-34.6196311450832),(-58.3522044331052,-34.6196327996266),(-58.3522135800151,-34.6196332063475),(-58.3522140905092,-34.6196330688896),(-58.3525470578217,-34.6195433134884),(-58.3525637568357,-34.6195388123538),(-58.3525640524421,-34.6195387323926),(-58.3525645847514,-34.6195385886429),(-58.3525649327152,-34.6195384952073),(-58.3525649555602,-34.6195385357927),(-58.3525651755558,-34.6195387379138),(-58.3525652398124,-34.6195387965654),(-58.3525653040679,-34.6195388561184),(-58.3525745545978,-34.6195557430233),(-58.3525830143123,-34.6195711851075),(-58.3526924458975,-34.6197709409727),(-58.3527500041595,-34.6197661413162),(-58.3529138030504,-34.6197533270398),(-58.352930095624,-34.6197511124415),(-58.352932016685,-34.6197471568507),(-58.3529320712126,-34.6197471514911),(-58.3530251120731,-34.6196191865927),(-58.3530847814238,-34.6195371208849),(-58.3535169906932,-34.6194050284189),(-58.353517020146,-34.6194050194309),(-58.3535170615979,-34.6194050068478),(-58.3535171247978,-34.6194050402576),(-58.3535171967433,-34.6194050565479),(-58.3535174202127,-34.6194051054257),(-58.3535922462841,-34.6194449745349),(-58.3537482066248,-34.6195280734073),(-58.3538908059641,-34.6196040532135),(-58.3539132658717,-34.6196160200227),(-58.3539569478602,-34.6196392944743),(-58.3540730580787,-34.6197011591484),(-58.3540733185057,-34.619701298202),(-58.3540735380644,-34.6197010018239),(-58.3542489671969,-34.6194641811712),(-58.3542489857667,-34.6194641559474),(-58.3542491310452,-34.6194639604642),(-58.3542493065901,-34.6194639687332),(-58.3542714924946,-34.619466123965),(-58.3542876699223,-34.6194676951289),(-58.3548157283979,-34.6195189864306),(-58.3550459687125,-34.61954135082),(-58.3550643943107,-34.6195431402104),(-58.3551396034653,-34.6195504460074),(-58.3551397652538,-34.6195501297447),(-58.3552004576535,-34.6194307028365),(-58.3552063037067,-34.6194185683012),(-58.3552119879448,-34.6194067698599),(-58.3553944096817,-34.619028133815),(-58.3554270639275,-34.6189603553423),(-58.3554944637746,-34.6188204579713),(-58.3556248892486,-34.6185278984876),(-58.3558089605165,-34.6181150021907),(-58.355850534169,-34.6180100758634),(-58.3558883697751,-34.6179145852235),(-58.3559543748521,-34.6177479992255),(-58.3559976557415,-34.6176387636499),(-58.3560102746336,-34.6176064769979),(-58.3560160949297,-34.6176125758213),(-58.3560232654914,-34.6176200901844),(-58.3560332040992,-34.6176305050964),(-58.3560387521663,-34.6176363197271),(-58.3565157277349,-34.6181361560189),(-58.3565288744756,-34.6181499324467),(-58.3573918896727,-34.6190542899696),(-58.3582680218934,-34.6199723661002),(-58.3594549091907,-34.6212160323007),(-58.3595018927039,-34.6212652617991),(-58.3595130028755,-34.6212769033708),(-58.3598634703814,-34.621644128395),(-58.3598650451181,-34.6216457775536),(-58.3600269818497,-34.6218154548566),(-58.3600296728513,-34.6218182741192),(-58.3601170820264,-34.6219098608689),(-58.3601175023933,-34.6219103020262),(-58.360163355179,-34.6219583458229),(-58.360374998092,-34.6221801036122),(-58.3603865190776,-34.6221921745325),(-58.3606576797422,-34.6224762910084),(-58.3606578071611,-34.6224764245281),(-58.3609519912748,-34.6227846622752),(-58.3609691646425,-34.6228026558019),(-58.3612324575063,-34.623078522556),(-58.3612336010249,-34.6230797215197),(-58.3612677301963,-34.6231154811464),(-58.3612726614929,-34.6231206477884),(-58.361285869702,-34.6231344877471),(-58.3615513460774,-34.6234126398616),(-58.3615868357779,-34.6234498238977),(-58.3615975816913,-34.6234610827638),(-58.3616236073543,-34.6234883503266),(-58.3616500436153,-34.6235160491118),(-58.3616609317498,-34.6235089484811),(-58.361778179848,-34.6236317935925),(-58.3617881667216,-34.6236422567444),(-58.3618696529468,-34.6237276327097),(-58.3619232043025,-34.623783740159),(-58.3619239927986,-34.62378456743),(-58.3619432238645,-34.6238047160547),(-58.361963663825,-34.623826131295),(-58.3620014507693,-34.6238657221445),(-58.361990562616,-34.6238728237065),(-58.3620162607198,-34.6238997483667),(-58.3623310268089,-34.6242295359895),(-58.3624180827247,-34.6243207457696),(-58.3624402273734,-34.6243439471789),(-58.3624624765873,-34.6243672586456),(-58.3625998580592,-34.6245111942349),(-58.362651118933,-34.6245648998483),(-58.3629296694069,-34.6248567380619),(-58.3630725960942,-34.6250064811072),(-58.3631955455644,-34.625135292504),(-58.3632547788916,-34.6251321118544),(-58.3633552481538,-34.6251267201837),(-58.3634548122451,-34.6251213772731),(-58.3634549856369,-34.625121372907),(-58.3635209971413,-34.6249900833532),(-58.3641528965732,-34.6246875569835),(-58.3648035451437,-34.6243174344487),(-58.3655003311068,-34.6239210592263),(-58.3657858460269,-34.6239873627789),(-58.3658398265419,-34.6237947933745),(-58.3658814572685,-34.6233055865918),(-58.3659303154823,-34.6227314329581),(-58.3659362168038,-34.6226620854143),(-58.3659664964511,-34.622395169837),(-58.3660670445222,-34.621508839012),(-58.3661902948305,-34.6204222098473),(-58.3663238692148,-34.6192449505585),(-58.366451415885,-34.618120152643),(-58.3665922125653,-34.6168790231657),(-58.3667344665838,-34.6156251471493),(-58.3668550140639,-34.6145771769023),(-58.3669896014429,-34.6133918883053),(-58.3670784887508,-34.6125975021372),(-58.3671273028888,-34.6121612484776),(-58.3672591297974,-34.6109984920666),(-58.3676179507285,-34.6078493963659),(-58.3676391138686,-34.6076636546245),(-58.3677246024109,-34.6069133549885),(-58.367725984598,-34.6069011198967),(-58.3679211193596,-34.6051742887552),(-58.3680475085269,-34.6040560355158),(-58.3681118473882,-34.6034865417202),(-58.3681856802166,-34.6028329984146),(-58.3683133529684,-34.601703195278),(-58.3683894892107,-34.6010295674968),(-58.3686314441,-34.6004359290355)]"

#Se lee la columna POLIGONOS de forma literal

Barrios['POLIGONOS'] = Barrios['POLIGONOS'].apply(lambda x: ast.literal_eval(x))

# Se convierten las coordenadas del DataFrame a objetos Polygon
Barrios['POLIGONOS'] = Barrios['POLIGONOS'].apply(lambda coords: Polygon(coords))

# Se crea un diccionario que mapea los nombres de barrios a los polígonos correspondientes
poligonos = dict(zip(Barrios['BARRIO'], Barrios['POLIGONOS']))

# La coordenada se pasa de la siguiente forma: (X,Y)

def determinar_barrio(coordenada):
    punto = Point(coordenada)

    for barrio, poligono in poligonos.items():
        if punto.within(poligono):
            return barrio

    return "No se encontró el barrio para estas coordenadas."