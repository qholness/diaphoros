import re

def country_parser(s):
	'''s is the source name.  We create an ASCII-only version, then lowercase,
	then look for distinct features.  We return FALSE if we cannot find anything.'''

	s = s.lower()

	if re.findall('andorra', s): return 'AD'
	elif re.findall('arab emirates', s): return 'AE'
	elif re.findall('afghanistan', s): return 'AF'
	elif re.findall('antigula', s): return 'AG' # barbuda as well?
	elif re.findall('anguilla', s): return 'AL' 
	elif re.findall('albania', s): return 'AL' 
	elif re.findall('armenia', s): return 'AM' 
	elif re.findall('angola', s): return 'AO' 
	elif re.findall('antarctica', s): return 'AQ' 
	elif re.findall('argentina', s): return 'AR' 
	elif re.findall('american samoa', s): return 'AS' 
	elif re.findall('austria', s): return 'AT' 
	elif re.findall('australia', s): return 'AU' 
	elif re.findall('aland', s): return 'AX' 
	elif re.findall('azerbaijan', s): return 'AZ' 
	elif re.findall('bosnia', s) or re.findall('herzegovina', s): return 'BA'
	elif re.findall('barbados', s): return 'BB'
	elif re.findall('bangladesh', s): return 'BD'
	elif re.findall('belgium', s): return 'BE'
	elif re.findall('burkina faso', s): return 'BF'
	elif re.findall('bulgaria', s): return 'BG'
	elif re.findall('bahrain', s): return 'BH'
	elif re.findall('burundi', s): return 'BI'
	elif re.findall('benin', s): return 'BJ'
	elif re.findall('barthelemy', s): return 'BL'
	elif re.findall('bermuda', s): return 'BM'
	elif re.findall('brunei darussalam', s): return 'BN'
	elif re.findall('bolivia', s): return 'BO'
	elif re.findall('bonaire', s): return 'BQ'
	elif re.findall('brazil', s): return 'BR'
	elif re.findall('bahamas', s): return 'BS'
	elif re.findall('bhutan', s): return 'BT'
	elif re.findall('botswana', s): return 'BW'
	elif re.findall('belarus', s): return 'BY'
	elif re.findall('belize', s): return 'BZ'
	elif re.findall('canada', s): return 'CA'
	#?! figure this one out.  kind of weird.
	# elif re.findall('cocos (keeling) island', s): return 'CC'
	#?! this probably subsets a few other places.
	# elif re.findall('the democratic republic of the congo', s): return 'CD'
	#?! this probably subsets a few other places.
	# elif re.findall('central african republic', s): return 'CF'
	#?! this probably subsets a few other places.
	#elif re.findall('congo', s): return 'CG'
	elif re.findall('switzerland', s): return 'CH'
	#?!other names for this one:
	elif re.findall("cote d'ivoire", s) or re.findall("ivoire", s): return 'CI'
	#?! this probably subsets a few other places.
	elif re.findall('cook islands', s): return 'CK'
	#?! this probably subsets a few other places.
	elif re.findall('chile', s): return 'CL'
	elif re.findall('cameroon', s): return 'CM'
	#?! this probably subsets a few other places.
	#elif re.findall('china', s): return 'CN'
	elif re.findall('colombia', s): return 'CO'
	elif re.findall('costa rica', s): return 'CR'
	#?! this probably subsets a few other places.
	#elif re.findall('cuba', s): return 'CU'
	elif re.findall('cape verde', s): return 'CV'
	elif re.findall('curacao', s): return 'CW'
	elif re.findall('christmas', s): return 'CX'
	elif re.findall('cyprus', s): return 'CY'
	elif re.findall('germany', s): return 'DE'
	elif re.findall('djibouti', s): return 'DJ'
	elif re.findall('denmark', s): return 'DK'
	# this should return dominican repub before dominica.
	elif re.findall('dominican republic', s): return 'DO'
	elif re.findall('dominica', s): return 'DM'
	elif re.findall('algeria', s): return 'DZ'
	elif re.findall('eduador', s): return 'EC'
	elif re.findall('estonia', s): return 'EE'
	elif re.findall('egypt', s): return 'EG'
	# weird name for this one...
	elif re.findall('western sahara', s): return 'EH'
	elif re.findall('eritrea', s): return 'ER'
	elif re.findall('spain', s): return 'ES'
	elif re.findall('ethiopia', s): return 'ET'
	elif re.findall('finland', s): return 'FI'
	elif re.findall('fiji', s): return 'FJ'
	# is this one true?
	elif re.findall('falkland', s) or re.findall('malvinas', s): return 'FK'
	elif re.findall('micronesia', s): return 'FM'
	elif re.findall('faroe', s): return 'FO'
	elif re.findall('france', s): return 'FR'

	else: return False