import xml.etree.ElementTree as ET


def parse_nmap_xml(xml_file):
    results = []

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for port in root.iter("port"):
            port_id = port.attrib.get("portid")

            state = port.find("state")
            if state is not None and state.attrib.get("state") == "open":
                service = port.find("service")

                service_name = service.attrib.get("name") if service is not None else "unknown"
                product = service.attrib.get("product") if service is not None else "unknown"

                results.append({
                    "port": int(port_id),
                    "service": service_name,
                    "product": product
                })

        return results

    except Exception as e:
        print(f"[-] Failed to parse XML {xml_file}: {e}")
        return []
