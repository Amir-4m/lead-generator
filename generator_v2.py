import datetime
import json
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class GeneratorService(object):
    def cookie(self, data=None):
        # Check if the JSON file exists
        json_filename = "./data.json"
        if not os.path.exists(json_filename):
            # Create the JSON file if it doesn't exist
            with open(json_filename, "w") as file:
                json.dump({}, file)

        # Data to be written into the JSON file

        # Read existing JSON data (if any)
        existing_data = {}
        with open(json_filename, "r") as file:
            existing_data = json.load(file)

        if data:
            existing_data.update(data)

            with open(json_filename, "w") as file:
                json.dump(existing_data, file, indent=4)
        return existing_data

    def get_text(self, elem):
        """
        Get Selenium element text

        Args:
            curElement (WebElement): selenium web element
        Returns:
            str
        Raises:
        """
        # # for debug
        # elementHtml = curElement.get_attribute("innerHTML")
        # print("elementHtml=%s" % elementHtml)

        elementText = elem.text  # sometime NOT work
        a = elem.get_attribute("innerText")
        b = elem.get_attribute("textContent")
        if not elementText:
            elementText = elem.get_attribute("innerText")

        if not elementText:
            elementText = elem.get_attribute("textContent")

        # print("elementText=%s" % elementText)
        return elementText

    def extract_web_auth_data(self):
        biotech = [
            "AUCTEQ Biosystems GmbH",
            "AVA LifeScience GmbH",
            "Axxam GmbH",
            "axxelera UG",
            "BAST GmbH",
            "BAV Institut für Hygiene und Qualitätssicherung GmbH",
            "BD Becton Dickinson GmbH",
            "BERTHOLD TECHNOLOGIES GmbH & Co. KG",
            "Greiner Bio-One GmbH",
            "Bioanalytic GmbH",
            "BioCat GmbH",
            "BioChem GmbH",
            "biochemA GmbH",
            "IBT - Immunological and Biochemical Testsystems GmbH",
            "BioCopy GmbH",
            "BioFluidix GmbH",
            "opto biolabs GmbH",
            "Reaction Biology Europe GmbH",
            "BMI Biomedical Informatics",
            "Meidrix Biomedicals GmbH",
            "biomers.net GmbH",
            "Biomex GmbH",
            "Rentschler Biopharma SE",
            "Octapharma Biopharmaceuticals GmbH",
            "BioRépair GmbH",
            "Q-bios GmbH",
            "Genaxxon BioScience GmbH",
            "CANDOR Bioscience GmbH",
            "Leica Biosystems Nussloch GmbH",
            "myPOLS Biotec GmbH",
            "VERAXA Biotech GmbH",
            "Sumaya Biotech GmbH & Co. KG",
            "PROGEN Biotechnik GmbH",
            "immatics biotechnologies GmbH",
            "VivaCell Biotechnology GmbH",
            "BioTeSys GmbH",
            "BioTina GmbH",
            "BioTissue Technologies GmbH",
            "BMG LABTECH GmbH",
            "Boehringer Ingelheim Therapeutics GmbH",
            "Boehringer Ingelheim Pharma GmbH & Co. KG",
            "Panatecs - a brand of Protagen Protein Services GmbH",
            "Gene Bridges GmbH",
            "PMCR GmbH - Precision Medicine and Cancer Research",
            "candidum GmbH",
            "CarboCode Germany GmbH",
            "CE-Immundiagnostika GmbH",
            "CeGaT GmbH",
            "CELL CONCEPTS GmbH",
            "CLS Cell Lines Service GmbH",
            "300MICRONS GmbH",
            "4base lab AG, advanced molecular analysis",
            "4HF Biotec GmbH",
            "AaviGen GmbH",
            "TOPATEC Wasser- und Abwassertechnik GmbH",
            "ACA CELL Biotech GmbH",
            "acousia Therapeutics GmbH",
            "ACQUIFER is a division of DITABIS\nDigital Biomedical Imaging Systems AG",
            "Actome GmbH",
            "Advanced Imaging Devices GmbH",
            "Affimed GmbH",
            "HB Technologies AG",
            "CureVac AG",
            "Metalife AG",
            "DITABIS Digital Biomedical Imaging Systems AG",
            "pantaBio AG",
            "Apogenix AG",
            "Heidelberg Pharma AG",
            "AHF analysentechnik AG",
            "Yokogawa Insilico Biotechnology GmbH (vormals Insilico Biotechnology AG)",
            "DIARECT AG",
            "TETEC Tissue Engineering Technologies AG",
            "WMT AG",
            "AGC Biologics GmbH",
            "Agilent Technologies Deutschland GmbH",
            "Agrano GmbH & Co. KG",
            "Eurofins Agroscience Services GmbH",
            "Allecra Therapeutics GmbH",
            "amcure GmbH",
            "STEFFENS BIOTECHNISCHE ANALYSEN GmbH",
            "C.A.T. GmbH & Co. Chromatographie und Analysentechnik KG",
            "HS Analysis GmbH",
            "SYMBIOSIS – The Analytical Company",
            "MAIER analytik GmbH",
            "Labor für DNA-Analytik",
            "Bioassay Labor für biologische Analytik GmbH",
            "ANASYN Dr. Ozan Gökay",
            "AnDiaTec Division\nQuidel Germany GmbH",
            "nadicom GmbH - Gesellschaft für angewandte Mikrobiologie mbH",
            "SD-nostik Bastian Schneider & Anne-Christin Schneider GbR",
            "anterio consult & research GmbH",
            "nanoTools Antikörpertechnik GmbH & Co. KG",
            "Antitoxin GmbH",
            "APARA-BIOSCIENCE GmbH",
            "RCA Reuter Chemische Apparatebau e.K.",
            "Aptamimetics GmbH",
            "Aquarray GmbH",
            "biosyn Arzneimittel GmbH",
            "ATG:biosynthetics GmbH",
            "Atriva Therapeutics GmbH",
            "Sartorius Stedim Cellca GmbH",
            "Cellendes GmbH",
            "Sartorius CellGenix GmbH",
            "Cellzome GmbH",
            "Celonic Deutschland GmbH & Co. KG",
            "ProtaGene CGT GmbH",
            "Multi Channel Systems MCS GmbH",
            "Charles River Discovery\nResearch Services Germany GmbH",
            "ORPEGEN Peptide Chemicals GmbH",
            "CLADE GmbH",
            "CLADIAC GmbH",
            "IKA®-Werke GmbH & Co. KG",
            "RHEACELL GmbH & Co. KG",
            "INTAVIS Peptide Services GmbH & Co. KG",
            "Hirschmann Laborgeräte GmbH & Co. KG",
            "MEDICHEM Diagnostica GmbH & Co. KG",
            "Hellma GmbH & Co. KG",
            "gerbion GmbH & Co. KG",
            "Computomics GmbH",
            "PreviPharma Consulting GmbH",
            "Corden Pharma GmbH",
            "Cubert GmbH",
            "Curetis GmbH",
            "cytena GmbH",
            "Cytolytics GmbH",
            "Heidelberg Delivery Technologies GmbH",
            "Dermagnostix GmbH",
            "Santhera Pharmaceuticals (Deutschland) GmbH",
            "Tentamus Pharma Med Deutsch­land GmbH",
            "Diagnostica GmbH Stuttgart",
            "Roche Diagnostics GmbH",
            "SOLIOS DIAGNOSTICS GmbH",
            "Hummingbird Diagnostics GmbH",
            "HiSS Diagnostics GmbH",
            "ravo Diagnostika GmbH",
            "Mediagnost Gesellschaft für Forschung und Herstellung von Diagnostika GmbH",
            "Protrans medizinische diagnostische Produkte GmbH",
            "Dialunox GmbH",
            "DiaMex GmbH",
            "Phytoplan Diehm & Neuberger GmbH",
            "Fast Forward Discoveries GmbH",
            "Dispendix GmbH",
            "DMT Produktentwicklung GmbH",
            "TherapySelect Dr. Frank Kischkel",
            "dsl-Labor",
            "DSM Nutritional Products GmbH",
            "Eurofins EAG Laboratories Ulm",
            "Efficient Robotics GmbH",
            "npi electronic GmbH",
            "SERVA Electrophoresis GmbH",
            "Eleva GmbH",
            "EMC microcollections GmbH",
            "EnFin GmbH",
            "Epimos GmbH",
            "Eurofins Genomics Europe Sequencing GmbH",
            "Eurofins LifeCodexx GmbH",
            "Eurofins | GeneScan GmbH",
            "Zymo Research Europe GmbH",
            "ExploSYS GmbH",
            "Thermo Fisher Scientific - Phadia GmbH",
            "FundaMental Pharma GmbH",
            "Hydrotox Labor für Ökotoxikologie und Gewässerschutz GmbH",
            "Generatio GmbH",
            "Genovac GmbH",
            "MetaSystems GmbH",
            "Synovo GmbH",
            "Herolab GmbH Laborgeräte",
            "KreLo GmbH",
            "Miltenyi Imaging GmbH",
            "menal GmbH",
            "Molecular Health GmbH",
            "NMI Technologietransfer GmbH",
            "MalVa GmbH",
            "Myomedix GmbH",
            "HepaRegeniX GmbH",
            "Lumobiotics GmbH",
            "Prime Vector Technologies GmbH",
            "KyooBe Tech GmbH",
            "IoLiTec Ionic Liquids Technologies GmbH",
            "Jobst Technologies GmbH",
            "SGS M-Scan GmbH",
            "Synthon GmbH",
            "TICEBA GmbH",
            "LOXO GmbH",
            "Nypro Healthcare GmbH",
            "Synimmune GmbH",
            "Zwisler Laboratorium GmbH",
            "ScreenFect GmbH",
            "Kiesel Steriltechnik GmbH",
            "Optima Testseren GmbH",
            "GoSilico GmbH",
            "HQS Quantum Simulations GmbH",
            "LABMaiTe GmbH",
            "LOGOPHARM GmbH",
            "instrAction GmbH",
            "Promega GmbH",
            "Trenzyme GmbH",
            "Repligen GmbH",
            "velixX GmbH",
            "JSI medical systems GmbH",
            "TolerogenixX GmbH",
            "Mireca Medicines GmbH",
            "PixelBiotech GmbH",
            "Variolytics GmbH",
            "Peptide Specialty Laboratories GmbH (PSL)",
            "Subitec GmbH",
            "WITec GmbH",
            "Hermle Labortechnik GmbH",
            "Hain Lifescience GmbH",
            "SOHENA GmbH",
            "VAXIMM GmbH",
            "IONERA Technologies GmbH",
            "Multiplexion GmbH",
            "highQu GmbH",
            "Poulten & Graf GmbH",
            "Klocke Verpackungs-Service GmbH",
            "SYNLAB MVZ Humangenetik Mannheim GmbH",
            "Luxendo GmbH",
            "Heidelberg ImmunoTherapeutics GmbH",
            "n.able GmbH",
            "Panosome GmbH",
            "HOT Screen GmbH",
            "PromoCell GmbH",
            "TEVA GmbH",
            "PEPperPRINT GmbH",
            "Polytec GmbH",
            "Katairo GmbH",
            "Sciomics GmbH",
            "PeptaNova GmbH",
            "HERBRAND PharmaChemicals GmbH",
            "SpinDiag GmbH",
            "Signatope GmbH",
            "Sensific GmbH",
            "KGW-Isotherm",
            "Rent-A-Lab",
            "Stratec SE"
        ]

        medtech = [
            "KUBIVENT GmbH",
            "LOXO GmbH",
            "Manfred Sauer GmbH",
            "Med-Tronik GmbH",
            "MRC Systems GmbH",
            "NeoMed Medizin Vertrieb + Logistik GmbH",
            "nopa instruments Medizintechnik GmbH",
            "REDA Instrumente GmbH",
            "Schreiber GmbH",
            "siema Siegfried Martin GmbH",
            "Stratec Medizintechnik GmbH",
            "Translumina GmbH",
            "Wilhelm Julius Teufel GmbH",
            "A. Milazzo Medizintechnik GmbH",
            "Willy Storz GmbH",
            "Stengelin Medical GmbH",
            "Werner Harfmann GmbH",
            "Paul Schöndorf Metallwaren GmbH",
            "Nypro Healthcare GmbH",
            "Koscher & Würtz GmbH",
            "medifa metall und medizintechnik GmbH",
            "Perpedes GmbH",
            "Novaliq GmbH",
            "Stockert GmbH",
            "Straumann GmbH",
            "medavis GmbH",
            "med3D GmbH",
            "MediBeacon GmbH",
            "Paradigm Spine GmbH",
            "Synthes Tuttlingen GmbH",
            "Nemera Neuenburg GmbH",
            "AS Medizintechnik GmbH",
            "NeuroClin Instruments GmbH",
            "Zeisberg GmbH",
            "NVT GmbH",
            "Kleinmann GmbH",
            "Soehnle Industrial Solutions GmbH",
            "Unbescheiden GmbH",
            "GRAMM medical healthcare GmbH",
            "Oertel + Lehner GmbH",
            "Optima Testseren GmbH",
            "Help Tech GmbH",
            "Hartmut Gärtner GmbH",
            "Helmut Schwarz GmbH",
            "HUWO Hydrotherapie GmbH",
            "Huonker GmbH",
            "Silony Medical GmbH",
            "Klaus Schuler GmbH Medizintechnik",
            "nemcomed GmbH medizin + wellness",
            "Instrumed GmbH",
            "KTJ Kunststofftechnik Junker GmbH",
            "Likamed GmbH",
            "Medilux Medizintechnik GmbH",
            "SUN Oberflächentechnik GmbH",
            "Henke-Sass, Wolf GmbH \nMedizin-technik Wenkert",
            "SII Technologies GmbH",
            "Innomedic GmbH",
            "QIT Systeme GmbH",
            "imed medical GmbH",
            "stimOS GmbH",
            "RUETSCHI Technology GmbH",
            "meQ GmbH",
            "pritidenta® GmbH",
            "Zana Technologies GmbH",
            "Medevo GmbH",
            "imm Innovative Medical Mannheim GmbH",
            "Hellstern medical GmbH",
            "Günter Stoffel Medizintechnik GmbH ( insto )",
            "Medical Service GmbH",
            "Sutter Medizintechnik GmbH",
            "Haux-Life-Support GmbH",
            "Kimetec GmbH",
            "medica Medizintechnik GmbH",
            "Precisemed GmbH",
            "TIM Tuttlinger Instrumenten Manufaktur GmbH",
            "TROKAMED GmbH",
            "zebris Medical GmbH",
            "ZEPF MEDICAL INSTRUMENTS GMBH",
            "Rominger Medizintechnik GmbH",
            "VeHu-Medical GmbH",
            "J.S.EVRO Instrumente GmbH",
            "Tuebingen Scientific Medical GmbH",
            "mediri GmbH",
            "VIREX GmbH",
            "Julius Wirth Inh. Josef Müller GmbH",
            "Mint Medical GmbH",
            "Trinon Titanium GmbH",
            "velixX GmbH",
            "Verapido Medical GmbH",
            "Heliocos GmbH",
            "Neurostar GmbH",
            "PRECISIS GmbH",
            "OPASCA GmbH",
            "Novotec Medical GmbH",
            "Prowital GmbH",
            "Görgü Medizintechnik GmbH",
            "SMI - Schad Medical Instruments GmbH",
            "JADENT GmbH",
            "Maxer Medizintechnik GmbH",
            "Sprintex Trainingsgeräte GmbH",
            "ORALIA medical GmbH",
            "redam-instrumente GmbH",
            "Invacare GmbH",
            "ResuSciTec GmbH",
            "Rhinolab GmbH",
            "sanawork GmbH",
            "Udo Meng GmbH",
            "Kenswick GmbH",
            "Leonair GmbH",
            "nubedian GmbH",
            "Mawendo GmbH",
            "HQ Imaging GmbH",
            "JOYY Mobility GmbH",
            "Kamedi GmbH",
            "Inovedis GmbH",
            "PAICON GmbH",
            "HEBUmedical GmbH",
            "Helmut Zepf Medizintechnik GmbH",
            "Manfred Schägner GmbH",
            "novineon Healthcare Technology Partners GmbH",
            "OptiMed Medizinische Instrumente GmbH",
            "Ortho Select GmbH",
            "ProXima Medical Systems GmbH",
            "Sänger GmbH",
            "Götz Service GmbH",
            "HATHO GmbH",
            "Hermle Labortechnik GmbH",
            "JOTEC GmbH",
            "Kastner Praxisbedarf GmbH",
            "MKW Lasersystem GmbH",
            "ORMED GmbH",
            "REIMERS & JANSSEN GmbH",
            "REMA Medizintechnik GmbH",
            "Richard Wolf GmbH",
            "Rudolf Riester GmbH",
            "Stuckenbrock Medizintechnik GmbH",
            "Hain Lifescience GmbH",
            "HGR Instrumente GmbH",
            "Reger Medizintechnik GmbH",
            "Rudolf Storz GmbH",
            "Schmid Medizintechnik GmbH",
            "Thomas Schumacher Micro-Instrumente GmbH",
            "Synthes GmbH",
            "InnoView GmbH",
            "MedXpert GmbH",
            "movisens GmbH",
            "UltraOsteon GmbH",
            "Nonvasiv Medical GmbH",
            "Vibrosonic GmbH",
            "MEXACARE GmbH",
            "mbits imaging GmbH",
            "MPS – Medizinische Planungssysteme GmbH",
            "Vincent Systems GmbH",
            "Seemann Technologies GmbH",
            "Humares GmbH",
            "Holzner GmbH",
            "PB MeTech GmbH",
            "Poulten & Graf GmbH",
            "Hellmut Ruck GmbH",
            "On-Lab GmbH",
            "Medentika Implant GmbH",
            "Medtro GmbH",
            "Merz Medizintechnik GmbH",
            "MI Med-Innovation GmbH",
            "Starmed GmbH",
            "uroclean®GmbH",
            "vmapit GmbH",
            "Thericon GmbH",
            "WiMedical GmbH",
            "HumanTech Spine GmbH",
            "Odilia Vision GmbH",
            "I.C.LERCHER-Solutions GmbH",
            "HuProMed GmbH",
            "medicalvalues GmbH",
            "Qatna Medical GmbH",
            "heckel medizintechnik GmbH",
            "PAJUNK GmbH",
            "Rebstock Instruments GmbH",
            "Greiner GmbH",
            "Hermann Medizintechnik GmbH",
            "HEIKO WILD GmbH Med. Instrumente",
            "inomed Medizintechnik GmbH",
            "MEDE Technik GmbH",
            "Metrax GmbH",
            "MONDEAL Medical Systems GmbH",
            "MORCHER GmbH",
            "Standard Textile GmbH",
            "Philipp Kirsch GmbH",
            "SCHOBER medicare GmbH",
            "UEBE Medical GmbH",
            "VascoMed GmbH",
            "Mayer Medizintechnik GmbH",
            "Raimund Wenzler GmbH",
            "Tontarra Medizintechnik GmbH",
            "MAQUET GmbH",
            "MEDARTIS GmbH",
            "livetec Ingenieurbüro GmbH",
            "Joimax GmbH",
            "Kreidler Medizintechnik GmbH",
            "LUMed GmbH",
            "Wenzler Medizintechnik GmbH",
            "Wellcomet GmbH",
            "Ortho Solutions GmbH",
            "Honburg Instrumente GmbH",
            "Ibenthaler GmbH",
            "Kleinbub Metall- und Kunststoffverarbeitung GmbH",
            "MEDI help Handel GmbH",
            "Standard Instruments GmbH",
            "SURGIWELL GmbH",
            "TBM Medizintechnik GmbH",
            "vlesia GmbH",
            "WellenGang GmbH",
            "MEDKLAPP Medizintechnik GmbH",
            "SpinDiag GmbH",
            "KLINGEL medical metal GmbH",
            "Sensific GmbH",
            "Mediteo GmbH",
            "Switch Mobility GmbH",
            "Perpedes Röck Gruppe",
            "Innovations Medical Gruppe",
            "Kas. Haiss KG",
            "IMP Innovative Medical Produkte Handelsgesellschaft mbH",
            "Hans-Karl Seid",
            "Heser Therapieliegen",
            "HG Micro Instrumente",
            "Honer Medizintechnik",
            "Klaus Huber Medizintechnik",
            "Müller-Instrumente",
            "Katz Medizintechnik",
            "Klaus Wenkert Medizintechnik",
            "LKS® Laboklinika Produktions- und Vertriebsgesellschaft mbH",
            "Lauf Medizintechnik und Sonderbau",
            "Marusits Medizintechnik OHG",
            "MTS Medical UG",
            "PSM Medical Solutions",
            "Noor Medical UG",
            "schätz meditec",
            "TMT Tschida Medizin Technik",
            "SR-Medizinelektronik",
            "Oertel Medizintechnik",
            "Zepf Medizintechnik",
            "Zientek Medizintechnik",
            "monikit UG",
            "Uwe Nudischer\nnudischer therapeutic textiles",
            "VILLINGER oHG",
            "RehaTechnik Stiefenhofer",
            "Stratec SE"
        ]
        queries = input('enter your queries (comma separated): ')
        queries = queries.split(',')
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        options = webdriver.ChromeOptions()
        path_to_extension = '/Users/enigma/Projects/lead-generator/ext'
        # options.headless = True
        options.add_argument('load-extension=' + path_to_extension)
        options.add_argument(f'--user-agent={user_agent}')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        service = Service(executable_path=ChromeDriverManager().install())
        dict_headers = self.cookie()
        if dict_headers:
            for key, value in dict_headers.items():
                options.add_argument(f"--header={key}: {value}")
        driver = webdriver.Chrome(service=service, options=options)
        actions = ActionChains(driver)
        driver.get(
            'https://www.linkedin.com/search/results/all/?keywords=(%22Business%20Case%20Service%22%20OR%20%22Disease%20Research%22)%20AND%20%22pharma%22&origin=HISTORY&sid=%40Lv')
        user_login = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/p/a')
        user_login.click()
        driver.find_element('id', 'username').send_keys('')  # todo EMAIL
        driver.find_element('id', 'password').send_keys('')  # todo PASSWORD
        driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
        time.sleep(20)
        for query in biotech:
            print(query)
            try:
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(5)
                search = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
                search.clear()
                search.send_keys(f'{query}')
                search.click()
                time.sleep(3)
                driver.find_element(By.XPATH, '//*[text() = "See all results"]').click()
                time.sleep(5)
                driver.find_element(By.XPATH, '//*[text() = "Companies"]').click()
                time.sleep(5)
                # Iterate through each li element and find the nested a element
                timer = datetime.datetime.now()
                try:
                    a_element = driver.find_elements(By.CLASS_NAME, "reusable-search__result-container")[0].find_element(By.CLASS_NAME, "app-aware-link")
                    actions.move_to_element(a_element).key_down(Keys.COMMAND).click(a_element).key_up(
                        Keys.COMMAND).perform()
                    time.sleep(5)
                    last_window_index = len(driver.window_handles) - 1
                    driver.switch_to.window(driver.window_handles[last_window_index])
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR,
                                        "a.ember-view.org-top-card-summary-info-list__info-item").click()
                    time.sleep(5)
                    driver.refresh()
                    time.sleep(10)
                    driver.find_element(By.CLASS_NAME, 'KLM_2726252_POPUP_OPEN').click()
                    time.sleep(5)
                    driver.find_element(By.CLASS_NAME, 'bind__837362622').click()
                    driver.switch_to.window(driver.window_handles[0])
                except Exception as e:
                    print(e)
                    if driver.window_handles.index(driver.current_window_handle) not in (0, 1):
                        driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    continue
            except:
                driver.switch_to.window(driver.window_handles[0])
                driver.get(
                    'https://www.linkedin.com/search/results/all/?keywords=(%22Business%20Case%20Service%22%20OR%20%22Disease%20Research%22)%20AND%20%22pharma%22&origin=HISTORY&sid=%40Lv')
                time.sleep(10)
                continue
        input("Press Enter to close the browser...")
        driver.quit()
